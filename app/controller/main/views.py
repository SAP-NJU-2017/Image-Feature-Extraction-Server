# -*- coding:utf-8 -*-
from . import app
from app import db
from app.models import User as user
from app.util import sap_api
from app.util import sliding_window
from app.util import file_helper
from flask import request
from PIL import Image
import requests
import json
import os
import shutil


# @app.route('/', methods=['GET'])
# def index():
#     temp = user.User.query.filter_by(username='test').first()
#     return json.dumps(temp, cls=user.UserEncode)
#
#
# @app.route('/add', methods=['GET'])
# def test():
#     new = user.User('test', 'this is a test case')
#     db.session.add(new)
#     db.session.commit()
#     return 'success'


@app.route('/try_api', methods=['GET'])
def try_api():
    filename = 'doc/Images/'
    filename = filename + request.args.get('name')  # ?key=value
    file = open(filename, 'rb')
    result = sap_api.image_feature_extraction(image=file)
    return result


@app.route('/try_product_classification_api', methods=['GET'])
def try_image_classification_api():
    filename = 'doc/Images/'
    filename = filename + request.args.get('name')  # ?key=value
    file = open(filename, 'rb')
    result = sap_api.image_classification(image=file)
    return result


@app.route('/try_similarity_scoring_api', methods=['GET'])
def try_similarity_scoring_api():
    filename = 'doc/Images/'
    filename = filename + request.args.get('name')  # ?key=value
    file = open(filename, 'rb')
    result = sap_api.similarity_scoring(image=file, options={"numSimilarVectors": 1})
    return result


# 前端调的方法
@app.route('/api/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        file.save(os.path.join("./doc/Images", filename=file.filename)) 
    return 'success'


@app.route('/api/find_error_area', methods=['GET'])
def find_error_area():
    filepath = "doc/Images/"+request.args.get('path')
    print(filepath)
    # TODO 获得框的位置和大小
    # image_model_path = "./doc/ImageModel/"
    # model_list = os.listdir(image_model_path)
    # for i in range(0, len(model_list)):
    #     model_path = os.path.join(image_model_path, model_list[i])
    #     model = Image.open(model_path)
    #     sliding_cut_list = sliding_window.slide(filepath, model.size[0], model.size[1], model.size[0] / 4,
    #                                             model.size[1] / 4)
    #     for cut in sliding_cut_list:
    #         cut_file = open(cut['startX'], 'rb')
    #         cut_feature = sap_api.image_feature_extraction(cut_file)
    #     model_name = model_path.split("/")
    #     image_collection = ["./doc/Vectors/" + model_name[len(model_name) - 1] + ".json"]

    # 将上传的图片整张和标准图片做特征向量相似性比较，得出与其相似度最高的一张标准图片
    target_feature_path = sap_api.image_feature_extraction_single(filepath)
    feature_collection = [target_feature_path]
    model_feature_dir_path = './doc/Vectors/'
    model_feature_list = os.listdir(model_feature_dir_path)

    for i in range(0, len(model_feature_list)):
        model_path = os.path.join(model_feature_dir_path, model_feature_list[i])
        feature_collection.append(model_path)

    if not os.path.exists("./doc/temp"):
        os.mkdir("./doc/temp")
    for file_path in feature_collection:
        shutil.copyfile(file_path, "./doc/temp/" + file_path.split("/")[-1])
    file_helper.zip_files("./doc/temp/*", 'featureZip.zip')
    feature_zip_file = open("featureZip.zip", 'rb')
    shutil.rmtree("./doc/temp")
    similarity_score = json.loads(sap_api.similarity_scoring(feature_zip_file))
    result_model_name = ''

    for prediction in similarity_score['predictions']:
        if prediction['id'] == filepath.split("/")[-1] + ".json":
            result_model_name = prediction['similarVectors'][0]['id']

    # 利用滑动窗口，找出上传图片中与标准图片最相似的部分
    feature_collection.clear()
    feature_collection.append("./doc/Vectors/" + result_model_name)
    image_model_path = "./doc/ImageModel/" + result_model_name.split(".json")[0]
    model = Image.open(image_model_path)
    sliding_cut_list = sliding_window.slide(filepath, model.size[0], model.size[1], 1 / 4,
                                            1 / 4)
    for cut_path in sliding_cut_list.keys():
        cut_feature_path = sap_api.image_feature_extraction_single(cut_path)
        feature_collection.append(cut_feature_path)

    if not os.path.exists("./doc/temp"):
        os.mkdir("./doc/temp")
    for file_path in feature_collection:
        shutil.copyfile(file_path, "./doc/temp/" + file_path.split("/")[-1])
    file_helper.zip_files("./doc/temp/*", 'featureZip.zip')
    feature_zip_file = open("featureZip.zip", 'rb')
    shutil.rmtree("./doc/temp")
    similarity_score = json.loads(sap_api.similarity_scoring(feature_zip_file))
    result_cut_name = ''

    for prediction in similarity_score['predictions']:
        if prediction['id'] == result_model_name:
            result_cut_name = prediction['similarVectors'][0]['id']

    sliding_window.clear_cut()

    result_cut_path = "./doc/SlideWindowCuts/" + result_cut_name.split(".json")[0]
    result = {'startx': sliding_cut_list[result_cut_path]['startX'],
              'starty': sliding_cut_list[result_cut_path]['startY'],
              'endx': sliding_cut_list[result_cut_path]['endX'],
              'endy': sliding_cut_list[result_cut_path]['endY']}

    return json.dumps(result)


# 获取错误信息
@app.route('/api/get_error_text', methods=['GET'])
def get_error_text():
    filepath = 'doc/Images/' + request.args.get('path')
    file = open(filepath, 'rb')
    result = sap_api.image_text_recognition(image=file)
    return result

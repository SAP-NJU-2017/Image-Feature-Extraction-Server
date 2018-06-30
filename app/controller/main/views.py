# -*- coding:utf-8 -*-
from . import app
from app import db
from app.models import User as user
from app.util import sap_api
from app.util import sliding_window
from flask import request
from PIL import Image
import requests
import json
import os


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
    result = sap_api.image_classification(image=file, options={"numSimilarVectors":1})
    return result


# 前端调的方法
@app.route('/find_error_area', methods=['GET'])
def find_error_area():
    filepath = request.args.get('path')
    # TODO 获得框的位置和大小
    image_model_path = "./doc/ImageModel/"
    model_list = os.listdir(image_model_path)
    for i in range(0, len(model_list)):
        model_path = os.path.join(image_model_path, model_list[i])
        model = Image.open(model_path)
        sliding_cut_list = sliding_window.slide(filepath, model.size[0], model.size[1], model.size[0]/4, model.size[1]/4)
        image_collection = []


    result = {'startx': 0, 'starty': 0, 'endx': 0, 'endy': 0}

    return json.dumps(result)

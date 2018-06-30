# -*- coding:utf-8 -*-
import requests
import json
import os
from .exception import NotImageError, PixelsTooLargeError


def image_feature_extraction(image):
    url = 'https://sandbox.api.sap.com/ml/featureextraction/inference_sync'
    data = {'enctype': 'multipart/form-data'}
    header = {'APIKey': 'xnXl9nIrNlSh30rVPcKwKjAjK9np9NjU'}
    files = {'files': image}
    response = requests.post(url=url, headers=header, data=data, files=files)
    text = response.text
    # print(text)
    return text


# 读取一个文件的向量并存下
# @param file 文件路径
def image_feature_extraction_single(file):
    vector = image_feature_extraction(open(file, 'rb'))
    if not file.endswith("png"):
        raise NotImageError("Uploaded file is not image")

    json_form = json.loads(vector)
    data = open(file + '.json', 'w+')

    if 'predictions' in json_form:
        vectors = json_form['predictions'][0]['feature_vector']
        string = "["
        for i in range(0, len(vectors)):
            string += str(vectors[i])
            if i < len(vectors) - 1:
                string += ","
            else:
                string += "]"
        data.write(string)
    else:
        print(file)
        raise PixelsTooLargeError("The pixels of image is too large")
    return file + ".json"


# 将一个目录下的所有图片都读取向量并存下
# @param dirt 目录路径
def image_feature_extraction_list(dirt):
    files = os.listdir(dirt)
    for i in range(0, len(files)):
        if not files[i].endswith("png"):
            continue

        path = os.path.join(dirt, files[i])
        try:
            image_feature_extraction_single(path)
        except (PixelsTooLargeError, NotImageError):
            pass


def image_classification(image):
    url = 'https://sandbox.api.sap.com/ml/imageclassifier/inference_sync'
    data = {'enctype': 'multipart/form-data'}
    header = {'APIKey': 'igGOBXHMjzg0JWXCAzaBdufp5YJyykHa'}
    files = {'files': image}
    response = requests.post(url=url, headers=header, data=data, files=files)
    text = response.text
    print(text)
    return text


def similarity_scoring(image):
    url = 'https://sandbox.api.sap.com/ml/similarityscoring/inference_sync'
    data = {'enctype': 'multipart/form-data'}
    header = {'APIKey': '2YeLfvAoIz1wuxuSkwLBLxHkJFkhKq0j'}
    files = {'files': image}
    response = requests.post(url=url, headers=header, data=data, files=files, options={"numSimilarVectors": 2})
    text = response.text
    print(text)
    return text


def image_text_recognition(image):
    url = 'https://sandbox.api.sap.com/ml/ocr/ocr'
    data = {'enctype': 'multipart/form-data'}
    header = {'APIKey': 'Jc3lKIOhWrIVRH8FuKPrJQRWiHrviuH6'}
    files = {'files': image}
    response = requests.post(url=url, headers=header, data=data, files=files,
                             options={"lang": "en", "output_type": "txt","page_seg_mode": "1", "model_type": "lstm_standard"})
    text = response.text
    print(text)
    return text

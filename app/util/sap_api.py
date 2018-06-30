# -*- coding:utf-8 -*-
import requests


def image_feature_extraction(image):
    url = 'https://sandbox.api.sap.com/ml/featureextraction/inference_sync'
    data = {'enctype': 'multipart/form-data'}
    header = {'APIKey': 'xnXl9nIrNlSh30rVPcKwKjAjK9np9NjU'}
    files = {'files': image}
    response = requests.post(url=url, headers=header, data=data, files=files)
    text = response.text
    print(text)
    return text


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

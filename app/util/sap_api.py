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
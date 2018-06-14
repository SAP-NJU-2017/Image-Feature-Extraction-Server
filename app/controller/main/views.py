# -*- coding:utf-8 -*-
from . import app
from app import db
from app.models import User as user
from app.util import sap_api
from flask import request
import json


@app.route('/', methods=['GET'])
def index():
    temp = user.User.query.filter_by(username='test').first()
    return json.dumps(temp, cls=user.UserEncode)


@app.route('/add', methods=['GET'])
def test():
    new = user.User('test', 'this is a test case')
    db.session.add(new)
    db.session.commit()
    return 'success'


@app.route('/try_api', methods=['GET'])
def try_api():
    filename = 'doc/Images/'
    filename = filename + request.args.get('name')  # ?key=value
    file = open(filename, 'rb')
    result = sap_api.image_feature_extraction(image=file)
    return result

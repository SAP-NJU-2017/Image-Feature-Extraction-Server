# -*- coding:utf-8 -*-
from . import app
from app import db
from app.models import User as user
import json


@app.route('/', methods=['GET'])
def index():
    test = user.User.query.filter_by(username='test').first()
    return json.dumps(test, cls=user.UserEncode)


@app.route('/add', methods=['GET'])
def test():
    new = user.User('test', 'this is a test case')
    db.session.add(new)
    db.session.commit()
    return 'success'

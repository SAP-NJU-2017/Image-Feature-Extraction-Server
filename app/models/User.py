# -*- coding:utf-8 -*-
from app import db
from json import JSONEncoder

class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String(20), nullable=False, primary_key=True)
    info = db.Column(db.String(80), nullable=False)

    def __init__(self, username, info):
        self.username = username
        self.info = info

    def __repr__(self):
        return '<User %r>' % self.username


class UserEncode(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            result = {'username': o.username, 'info': o.info}
            return result
        return JSONEncoder.default(self, o)
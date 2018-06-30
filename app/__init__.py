# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 按照你们数据库配置来修改此项 mysql://用户名:密码@服务器地址:端口号/数据库名称
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:hello@localhost:3306/sap'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
db.init_app(app)

from .controller.main import app as main
app.register_blueprint(main)

# -*- coding:utf-8 -*-
from flask_script import Manager
from app import app

manager = Manager(app)
manager.run()


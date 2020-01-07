# -*- coding: utf-8 -*-
# @File    : __init__.py
# 描述     ：
# @Time    : 2020/1/7
# @Author  :
# @QQ      :
from flask import Flask


from .settings import config
from .extensions import init_app

from .views import register_blueprint
from .admin import dog_blueprint
# from App.views.user import user
# from App.views import bbs

# 创建应用程序对象
def create_app():
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(config.get('develop','default'))

    # 加载扩展
    init_app(app)

    #注册蓝图
    register_blueprint(app)
    dog_blueprint(app)

    return app


# -*- coding: utf-8 -*-
# @File    : settings.py
# 描述     ：应用配置文件
# @Time    : 2020/1/7
# @Author  : 
# @QQ      :

#基础配置文件
class BaseConfig:
    DEBUG = False
    SECRECT_KEY = '72590f76-3115-11ea-b8b1-9801a78d7440'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
# 开发环境
class DevelopConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456.@127.0.0.1:3306/py1910"

# 生成环境（线上）
class ProductConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456.@127.0.0.1:3306/py1910"

config = {
    'default':BaseConfig,
    'develop':DevelopConfig,
    'production':ProductConfig
}
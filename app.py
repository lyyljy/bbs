# -*- coding: utf-8 -*-
# @File    : app.py
# 描述     ：
# @Time    : 2020/1/7
# @Author  : 
# @QQ      :


from flask import Flask
from flask_script import Manager
from flask_migrate import MigrateCommand

from App import create_app

app = create_app()
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
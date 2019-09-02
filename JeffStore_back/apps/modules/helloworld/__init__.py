# -*- coding: UTF-8 -*-
"""
__author__: jack
__date__:2019/9/1 16:02
"""
from flask import Blueprint

# 1.创建蓝图对象
hello_bp = Blueprint("helloworld", __name__)

# 3.让包知道views文件中的视图函数
from apps.modules.helloworld.views import *
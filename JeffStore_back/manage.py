# -*- coding: UTF-8 -*-
"""
__author__: jack
__date__:2019/9/1 14:27
"""
import sys
import os
from flask import jsonify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 添加导包路径
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

from apps import create_app


app = create_app("development")

if __name__ == '__main__':
    app.run()
# @app.route('/')
# def route_map():
#     """
#     主视图，返回所有视图网址
#     """
#     rules_iterator = app.url_map.iter_rules()
#     return jsonify({rule.endpoint: rule.rule for rule in rules_iterator if rule.endpoint not in ('route_map', 'static')})
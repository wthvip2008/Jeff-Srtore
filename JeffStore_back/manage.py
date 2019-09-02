# -*- coding: UTF-8 -*-
"""
__author__: jack
__date__:2019/9/1 14:27
"""
import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 添加导包路径
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

from apps import create_app


app = create_app("development")

if __name__ == '__main__':
    app.run()
# -*- coding: UTF-8 -*-
"""
__author__: jack
__date__:2019/9/1 14:27
"""
from apps import create_app


app = create_app("development")

if __name__ == '__main__':
    app.run()
# -*- coding: UTF-8 -*-
"""
__author__: jack
__date__:2019/9/1 16:04
"""
from apps.modules.helloworld import hello_bp


@hello_bp.route('/')
def hello_world():
    return 'hello world'


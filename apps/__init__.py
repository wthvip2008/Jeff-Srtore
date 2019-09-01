# -*- coding: UTF-8 -*-
"""
__author__: jack
__date__:2019/9/1 14:28
"""
from flask import Flask
from apps.config import config_list


# 将app封装起来，给外界调用提供一个接口方法：create_app
def create_app(config_name):
    """
    将与app相关联的配置封装到`工厂方法`中
    :param config_name: 配置文件
    :return: app对象
    """
    app = Flask(__name__)
    # 根据development键获取对应的配置类名
    config = config_list[config_name]
    app.config.from_object(config)

    # 测试用的hellpworld
    from apps.modules.helloworld import hello_bp
    app.register_blueprint(hello_bp)

    return app

# -*- coding: UTF-8 -*-
"""
__author__: jack
__date__:2019/9/1 14:49
"""
import logging
from pymongo import MongoClient
from redis import StrictRedis


class Config():
    # 通用ip
    host = '127.0.0.1'
    # mongdb端口
    mongodb_port = 27017
    # redis_port
    redis_port = '6379'
    # 配置mongodb对象
    mongodb_client = MongoClient(host,mongodb_port)
    # 配置mongodb集合对象
    collection = mongodb_client.JeffStore.stu
    # 配置redis数据库对象
    redis_client = StrictRedis(host='localhost', port=redis_port, db=0)


class DevelopmentConfig():
    """开发模式的配置类"""
    DEBUG = True
    # 设置日志的级别
    LOG_LEVEL = logging.DEBUG


class ProductionConfig():
    """线上模式的配置类"""

    DEBUG = False
    # 设置日志的级别
    LOG_LEVEL = logging.ERROR


# 给外界使用提供一个接口
config_list = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
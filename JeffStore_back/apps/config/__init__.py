# -*- coding: UTF-8 -*-
"""
__author__: jack
__date__:2019/9/1 14:49
"""
import logging
from pymongo import MongoClient
from redis import StrictRedis


class Config():

    MONGODB_HOST = '127.0.0.1'
    REDIS_HOST = '127.0.0.1'
    # mongdb端口
    MONGODB_POST = 27017
    # redis_port
    REDIS_PORT = '6379'
    # 配置mongodb对象
    mongodb_client = MongoClient(MONGODB_HOST,MONGODB_POST)
    # 配置mongodb集合对象
    collection = mongodb_client.JeffStore.stu

    # mysql数据库配置信息
    # 连接mysql数据库的配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/jeff"
    # 开启数据库跟踪模式
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 开启数据库自动提交功能
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class DevelopmentConfig(Config):
    """开发模式的配置类"""
    DEBUG = True
    # 设置日志的级别
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(Config):
    """线上模式的配置类"""

    DEBUG = False
    # 设置日志的级别
    LOG_LEVEL = logging.ERROR


# 给外界使用提供一个接口
config_list = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
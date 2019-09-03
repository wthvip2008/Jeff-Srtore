# -*- coding: UTF-8 -*-
"""
__author__: jack
__date__:2019/9/1 14:28
"""
from flask import Flask
from JeffStore_back.apps.config import config_list
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
import logging
from logging.handlers import RotatingFileHandler
from JeffStore_back.apps.config import DevelopmentConfig


# 只是申明了db对象而已，并没有做真实的数据库初始化操作
db = SQLAlchemy()

# 将redis数据库对象申明成全局变量
# # type:StrictRedis 提前申明redis_store数据类型
redis_store = None  # type:StrictRedis


def get_logger(config_class):
    """
    配置日志同时输出至文件及屏幕
    :param config_name: 开发模式或者线上模式
    :return: logger日志输出器对象
    """
    # 创建一个logger对象，它提供了应用程序可以直接使用的接口
    logger = logging.getLogger(__name__)

    # 创建文件流：指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 定义文件输出流的告警级别
    file_log_handler.setLevel(level=config_class.LOG_LEVEL)

    # 创建屏幕输出流
    screen_log_handler = logging.StreamHandler()
    # 定义屏幕输出流的告警级别.默认debug
    screen_log_handler.setLevel(logging.DEBUG)

    # 创建日志记录的格式: 时间 日志等级 输入日志信息的文件名   行数  日志信息
    #              Time    DEBUG  index.py           100   name
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d %(message)s')

    # 设置文件输出格式及屏幕输出格式
    file_log_handler.setFormatter(formatter)
    screen_log_handler.setFormatter(formatter)

    # 为全局添加日志记录器
    logger.addHandler(file_log_handler)
    logger.addHandler(screen_log_handler)

    # 返回logger 为了自定义添加日志信息
    return logger

# 提供个日志对象，方式全局使用
logger = get_logger(DevelopmentConfig)

def create_app(config_class):
    """
    将与app相关联的配置封装到`工厂方法`中,给外界调用提供一个接口方法：create_app
    :param config_name: 配置文件
    :return: app对象
    """
    app = Flask(__name__)
    # 根据development键获取对应的配置类名
    config = config_list[config_class]
    app.config.from_object(config)

    # 记录日志
    get_logger(config)

    # 创建mysql数据库对象:延迟加载，懒加载思想，当app有值的时候才进行真正的初始化操作
    db.init_app(app)
    # 3.创建redis数据库对象(懒加载的思想)
    global redis_store
    redis_store = StrictRedis(host=config.REDIS_HOST,
                              port=config.REDIS_PORT,
                              decode_responses=True
                              )
    """redis_store.set("age", 18)  ---->默认存储到redis ---0号数据库"""


    # 测试用的hellpworld
    from JeffStore_back.apps.modules.helloworld import hello_bp
    app.register_blueprint(hello_bp)


    return app

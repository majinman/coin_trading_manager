#-*- coding:utf-8 -*-
# todo json 파일에 저장해서 불러와서 입력하
import os
import json


class DevelopmentConfig():
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:[PASSWORD]@localhost/coinsys?charset=utf8"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "dsdfsdfsdfsdfsdf"
    DEBUG = True
    IS_PRODUCTION = False




def getConfig():
    return DevelopmentConfig()

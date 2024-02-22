import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY = "pepe contraseña"
    SESSION_COOKIE_SECURE = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://Salvador:Pepeshava_02@127.0.0.1/bdidgs081'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
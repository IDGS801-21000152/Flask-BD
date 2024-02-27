import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY = "pepe contraseña"
    SESSION_COOKIE_SECURE = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    ## Creamos la base de datos en el gestor
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://Salvador:Pepeshava_02@127.0.0.1/bdidgs801'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
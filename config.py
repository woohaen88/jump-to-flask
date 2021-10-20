import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@testdb/ururu?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'zoo-app-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'database-zoo-app'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'adminzooapp'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Password!1@2'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'storagezooapp'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'UP7P5dBiww5pcDHPYLhhyKBfCAAdo2YstVoH1dy1wUBMz4yvGJrYqd1xoIW3a8hbg2yOJZSAW7Qpj45+JNaqYA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

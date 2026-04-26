import os
from urllib.parse import quote_plus
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cms-secret-key-2024'
    SQL_SERVER    = os.environ.get('SQL_SERVER')
    SQL_DATABASE  = os.environ.get('SQL_DATABASE')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD  = os.environ.get('SQL_PASSWORD')

    _pwd = quote_plus(os.environ.get('SQL_PASSWORD') or '')
    _user = os.environ.get('SQL_USER_NAME') or ''
    _server = os.environ.get('SQL_SERVER') or ''
    _db = os.environ.get('SQL_DATABASE') or ''

    SQLALCHEMY_DATABASE_URI = (
        f'mssql+pyodbc://{_user}:{_pwd}@{_server}:1433/{_db}'
        '?driver=ODBC+Driver+17+for+SQL+Server'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT     = os.environ.get('BLOB_ACCOUNT')
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONTAINER   = os.environ.get('BLOB_CONTAINER')
    CLIENT_ID     = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    AUTHORITY     = 'https://login.microsoftonline.com/common'
    REDIRECT_PATH = '/getAToken'
    SCOPE         = ['User.Read']
    SESSION_TYPE  = 'filesystem'

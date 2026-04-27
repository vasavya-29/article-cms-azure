"""
The flask application package.
"""
import logging
import os
import pyodbc
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from flask.logging import create_logger
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

app = Flask(__name__)
app.config.from_object(Config)

# Override DB connection using explicit pyodbc params
connection_url = URL.create(
    'mssql+pyodbc',
    username=os.environ.get('SQL_USER_NAME'),
    password=os.environ.get('SQL_PASSWORD'),
    host=os.environ.get('SQL_SERVER'),
    port=1433,
    database=os.environ.get('SQL_DATABASE'),
    query={'driver': 'ODBC Driver 17 for SQL Server'}
)
app.config['SQLALCHEMY_DATABASE_URI'] = connection_url

LOG = create_logger(app)
LOG.setLevel(logging.INFO)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)
LOG.addHandler(streamHandler)
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
import FlaskWebProject.views

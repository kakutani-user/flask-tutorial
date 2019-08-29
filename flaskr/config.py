import os
SQLALCHEMY_DATABASE_URI = 'sqlite:///flaskr.db'
SQLALCHEMY_TRACK_MODIFICATIONS = "True"
SECRET_KEY = os.urandom(24)
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///api.db'
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'cover')


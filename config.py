import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///api.db'
    COVERS_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/covers')


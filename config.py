import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://imma:1234@localhost/pitchit'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    DATABASE_URL=os.environ.get("DATABASE_URL")

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
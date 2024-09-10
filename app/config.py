import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://user:password@localhost/mi_base_de_datos')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

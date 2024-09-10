from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar base de datos
    db.init_app(app)
    
    return app

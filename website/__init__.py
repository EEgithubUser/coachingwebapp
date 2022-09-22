# this makes the "website" folder a python package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file)

db = SQLAlchemy()
DB_NAME = "database.db"

# Create flask applicaton, initialize secret key, return it from the function
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config['SECRET_KEY']['key']
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Weight, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')



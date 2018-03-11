# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_pagedown import PageDown
from config import config


bootstrap = Bootstrap()
db = SQLAlchemy(use_native_unicode='utf8')
mail = Mail()
moment = Moment()
login_manager = LoginManager()
login_manager.session_protection = 'string'
login_manager.login_view = 'auth.login'
pagedown = PageDown()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config['production'])
    config['production'].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)

    from .main import main as main_buleprint
    app.register_blueprint(main_buleprint)

    from .auth import auth as auth_buleprint
    app.register_blueprint(auth_buleprint, url_prefix='/auth')

    return app

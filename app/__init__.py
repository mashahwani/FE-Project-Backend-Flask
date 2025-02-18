
from flask import Flask
from app.routes.views import users_bp
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(users_bp, url_prefix='/api')

    return app

from flask import Flask


def create_app() -> Flask:
    app: Flask = Flask(__name__)

    from .views.routes import api

    app.register_blueprint(api)

    return app

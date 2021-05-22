from flask import Flask
import secrets


def create_app() -> Flask:
    app = Flask(__name__)

    from . import index
    app.register_blueprint(index.bp)

    secret = secrets.token_urlsafe(32)
    app.secret_key = secret

    return app

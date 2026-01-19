from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.routes import subscribe

    app.register_blueprint(subscribe.bp)

    return app

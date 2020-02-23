from flask import Flask


def create_app():
    app = Flask(__name__)
    with app.app_context():
        from app.home import home
        app.register_blueprint(home)
    app.app_context().push()

    return app

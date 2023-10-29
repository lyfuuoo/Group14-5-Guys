from flask import Flask

from routes.user_authentication_system import user
from routes.detailed_system import detail


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user)
    app.register_blueprint(detail)
    return app


from flask import Flask
from pypokeragile.ext import configuration

#usable for test purposes
def minimal_app():
    app = Flask(__name__)
    configuration.ini_app(app)
    return app


def create_app():
    app = minimal_app()
    configuration.load_extensions(app)
    return app




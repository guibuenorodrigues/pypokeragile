from flask import Blueprint
from pypokeragile.ext import socketio
from .events import init_events_handler

bp = Blueprint("room", __name__, url_prefix='/room')
socket_io = socketio.sio

def init_app(app):
    app.register_blueprint(bp)
    init_events_handler(socket_io)


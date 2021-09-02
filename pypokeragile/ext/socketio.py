from flask_socketio import SocketIO

sio = SocketIO(cors_allowed_origins='*')

def run_app(app):
    sio.run(app)

def init_app(app):
    sio.init_app(app)
    run_app(app)

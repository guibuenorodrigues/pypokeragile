from . import rooms

base_path = '/api/v1'


def init_app(app):
    app.register_blueprint(rooms.rooms_bp, url_prefix=base_path + '/rooms')

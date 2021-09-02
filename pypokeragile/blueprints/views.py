import hashlib
from flask import render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from pypokeragile.ext.database import Rooms


def init_app(app):

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/create-room")
    def create_room():
        return render_template("create_room.html")

    @app.route("/join-room")
    def join_room():
        return render_template("join_room.html")

    @app.route("/game-room/<string:room_key>")
    def game_room(room_key: str = None):

        # get room data and then import it
        room = Rooms.get_by_key(room_key)

        if room is None:
            return redirect(url_for(".create_room"))

        if len(room.password) > 0:
            return "<h1>you need an password to access the room!</h1>"
        
        rfc_param = request.args.get('rfc')
        

        rfc_hash = hashlib.sha1('{0}_{1}_{2}'.format(room_key, room.owner_name, room.owner_email).encode()).hexdigest()
        is_admin = (rfc_hash == rfc_param)
        
        return render_template(
            "game_room.html",
            room_key=room_key,
            room_name=room.name,
            owner_name=room.owner_name,
            room_admin=is_admin)

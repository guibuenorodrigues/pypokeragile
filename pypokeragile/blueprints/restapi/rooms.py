from pypokeragile.blueprints.restapi.helpers import prepare_response_json, redirect_view
from flask import Blueprint, jsonify, redirect, request
from flask.helpers import url_for
from flask_restful import Api
from pypokeragile.ext.database import Rooms
from uuid import uuid4
import hashlib

rooms_bp = Blueprint('rooms_bp', __name__)
Api(rooms_bp)


@rooms_bp.route("/create", methods=['POST'])
def create_room():
    header_x_content_type = request.headers.get('x-content-type')
    x_content_type = 'restful' if header_x_content_type is None else header_x_content_type

    message = {}

    data = request.get_json()

    if not data:
        message['error'] = 'you need to provide the json content'
        return message, 400

    if 'room_name' not in data or data['room_name'] == '':
        message['error'] = 'you need to provide the name of the room'
        return message, 400

    room_uuid = str(uuid4())[:5]
    room_name = data['room_name']
    owner_name = data['owner_name'] if 'owner_name' in data else ''
    owner_email = data['owner_email'] if 'owner_email' in data else ''
    room_password = data['room_password'] if 'room_password' in data else ''

    success = True
    try:
        room = Rooms(room_name, room_uuid)
        room.owner_name = owner_name
        room.owner_email = owner_email
        room.password = room_password
        room.save()
    except Exception as e:
        success = False
        print(e)

    if x_content_type == 'view':
        if success:
            rfc_object = hashlib.sha1('{0}_{1}_{2}'.format(room_uuid, owner_name, owner_email).encode())

            return redirect_view("game_room", room_key=room_uuid, rfc=rfc_object.hexdigest())
        else:
            print('error to save room')
            pass
    else:
        if success:
            res = {
                "room_key": room_uuid,
                "room_name": room_name,
                "owner_name": owner_name,
                "owner_email": owner_email
            }

            return prepare_response_json(201, json_content=res, message='your room was created')
            


@rooms_bp.route("/join/<room_key>", methods=['POST'])
def join_room(room_key: str = None):
    x_content_type = request.headers.get('x-content-type')

    message = {}

    # if x_content_type is None or x_content_type != 'view':
    #     message['error'] = "the resource is not implemented without a view"
    #     return message, 501

    if room_key is None:
        message['error'] = "please provide an room key"
        return message, 400

    data = request.get_json()

    print(data)
    if not data:
        message['error'] = 'you need to provide the json content'
        return message, 400

    if 'room_name' not in data or data['room_name'] == '':
        message['error'] = 'you need to provide the name of the room'
        return message, 400

    room_uuid = str(uuid4())[:5]

    if x_content_type == 'view':
        return redirect(url_for("game_room", room_key=room_uuid))
    else:
        return jsonify(
            {
                "room_key": room_uuid,
                "room_name": data['room_name'],
                "email": data['email'] if 'email' in data else ''
            }
        )

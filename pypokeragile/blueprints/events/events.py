from flask_socketio import SocketIO, emit

def init_events_handler(socket_io: SocketIO):

    # @socket_io.on('connect')
    # def handle_connect(content):
    #     print(content)

    @socket_io.on('sendMessage')
    def handle_send_message(message):
        print(message)
    

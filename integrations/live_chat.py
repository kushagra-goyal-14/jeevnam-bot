def register_live_chat(socketio):
    @socketio.on('my event')
    def handle_my_custom_event(payload):


        if not isinstance(payload, dict):
            return
        name = payload.get('user_name')

        message = payload.get('message')
        if not isinstance(name, str) or not isinstance(message, str):
            return
        name, message = name.strip(), message.strip()
        if not name or not message or len(name) > 80 or len(message) > 2000:
            return


        # send to everyone conected
        socketio.emit('my response', {'user_name': name, 'message': message})

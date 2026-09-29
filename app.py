import os
import secrets

from flask import Flask, render_template
from flask_socketio import SocketIO

from integrations.health_chatbot import chatbot
from integrations.live_chat import register_live_chat

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or secrets.token_hex(32)
app.register_blueprint(chatbot)
socketio = SocketIO(app, async_mode='threading')
register_live_chat(socketio)


@app.route('/')
@app.route('/chat')
def chat():
    return render_template('chat.html')


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=8080)

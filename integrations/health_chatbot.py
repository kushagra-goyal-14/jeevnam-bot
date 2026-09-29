import os
from uuid import uuid4

import requests
from flask import Blueprint, request, session

chatbot = Blueprint('health_chatbot', __name__)


@chatbot.route('/bothook')
def get_bot_response():
    message = request.args.get('msg', '').strip()
    if not message:
        return 'Please enter a message.', 400
    if len(message) > 2000:
        return 'Please keep messages under 2,000 characters.', 400
    if 'rasa_sender' not in session:
        session['rasa_sender'] = str(uuid4())
    try:
        response = requests.post(
            os.environ.get('RASA_URL', 'http://localhost:5005/webhooks/rest/webhook'),
            json={'sender': session['rasa_sender'], 'message': message},
            timeout=20,
        )
        response.raise_for_status()
        # read bot replys
        replies = response.json()
        if not isinstance(replies, list):
            raise ValueError('Unexpected Rasa response')
        text = '\n'.join(
            reply['text'] for reply in replies
            if isinstance(reply, dict) and isinstance(reply.get('text'), str)
        )
        return text or 'Please try rephrasing your question.'
    except (requests.RequestException, ValueError):
        return 'The health chatbot is unavailable. Please try again later.', 502

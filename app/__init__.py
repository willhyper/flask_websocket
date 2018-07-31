from flask import Flask
from flask_socketio import SocketIO, emit

flask_app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(flask_app)

from functools import partial
from_backend_to_frontend = partial(socketio.emit, 'from_backend_to_frontend', namespace='/test')

import app.views
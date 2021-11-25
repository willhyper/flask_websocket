from flask import Flask
from flask_socketio import SocketIO, emit

flask_app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(flask_app)

import app.views
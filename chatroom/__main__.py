from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, disconnect


app = Flask(__name__)
socketio = SocketIO(app)


def send(msg):
    emit('my_response', {'send':msg})

def broadcast(msg):
    emit('my_response', {'broadcast': msg}, broadcast=True)


@socketio.on('my_broadcast_event', namespace='/test')
def test_broadcast_message(message):
    broadcast(message['data'])


@socketio.on('disconnect_request', namespace='/test')
def disconnect_request():
    send('Disconnected!')
    disconnect()


@socketio.on('connect', namespace='/test')
def test_connect():
    send('Connected!')


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0',port=8080, debug=True)

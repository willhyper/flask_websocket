import time
from threading import Thread
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

from functools import partial

from_backend_to_frontend = partial(socketio.emit, 'from_backend_to_frontend', namespace='/test')


def background_stuff():
    """ Let's do it a bit cleaner """
    while True:
        time.sleep(1)
        t = str(time.clock())
        from_backend_to_frontend({'message': 'tic toc', 'time': t})


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('from_frontend_to_backend', namespace='/test')
def my_event(msg):
    print(msg)


@socketio.on('connect', namespace='/test')
def on_connect():
    # emit('my response', {'data': 'Connected', 'count': 0})
    from_backend_to_frontend({'message': 'connected'})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    Thread(target=background_stuff, daemon=True).start()
    socketio.run(app, host='0.0.0.0', port=8888, debug=True)


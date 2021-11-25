from flask import render_template, request, json
from . import flask_app, socketio


def from_backend_to_frontend(msg):
    socketio.emit('from_backend_to_frontend', msg, namespace='/test')

@flask_app.route('/', methods=['GET', ])
def index():
    return render_template('index.html')


@flask_app.route('/send', methods=['GET', ])
def send():
    msg = request.args.get('message', None)
    if msg:
        from_backend_to_frontend({'message':msg})        
    return json.dumps({'message sent':msg})


@socketio.on('from_frontend_to_backend', namespace='/test')
def my_event(msg):
    print(msg)


@socketio.on('connect', namespace='/test')
def on_connect():
    from_backend_to_frontend({'message': 'connected'})



@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

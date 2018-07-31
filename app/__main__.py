from . import socketio, flask_app

socketio.run(flask_app, host='0.0.0.0', port=8888)



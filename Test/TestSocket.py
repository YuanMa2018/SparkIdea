<<<<<<< HEAD
#!/usr/bin/env python
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index2.html')


@socketio.on('client_event')
def client_msg(msg):
    emit('server_response', {'data': msg['data']})


@socketio.on('connect_event')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})


if __name__ == '__main__':
=======
#!/usr/bin/env python
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index2.html')


@socketio.on('client_event')
def client_msg(msg):
    emit('server_response', {'data': msg['data']})


@socketio.on('connect_event')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})


if __name__ == '__main__':
>>>>>>> 6a9a1f8897db0d7c063476224d81cec9aa98e922
    socketio.run(app)
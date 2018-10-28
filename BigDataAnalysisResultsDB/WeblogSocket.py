#!/usr/bin/env python
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
from WeblogService import WeblogService
import time
import json

app = Flask(__name__, template_folder='../templates',static_folder='../templates/js')
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('showData.html')

@app.route('/test')
def test():
    return render_template('EchartTest.html')

@socketio.on('client_event')
def client_msg(msg):
    i = 1
    while True:
        w = WeblogService()
        titleNames = w.queryWeblogs()['titleNames']
        titleCounts = w.queryWeblogs()['titleCounts']
        titleSum = w.TotalTitleCount()
        retMap = {'titleNames': titleNames, 'titleCounts': titleCounts, 'titleSum': titleSum};
        emit('server_response', {'data': json.dumps(retMap)})
        time.sleep(1)
        i = i + 1
        if i == 10:
            break



@socketio.on('connect_event')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})


if __name__ == '__main__':
    socketio.run(app)





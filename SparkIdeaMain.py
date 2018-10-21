# coding:utf-8
from flask import Flask, session, render_template, redirect, url_for, request

import config
from extensions import db
from models import User
from flask_socketio import SocketIO, emit
from BigDataAnalysisResultsDB.WeblogService import WeblogService
import time
import json
import BigData_NewsSourceInput
import threading
app = Flask(__name__,template_folder='./templates',static_folder='./templates/js')
app.config.from_object(config)
db.init_app(app)
socketio = SocketIO(app)



with app.app_context():
    db.create_all()



@app.route('/', methods=['GET', 'POST'])
def index():
    # Result = User.query.filter(1==1).order_by(-User.id).all()
    # print(Result)
    login_url = url_for('SparkIdeaRegister')
    return redirect(login_url)
    # return str(Result[0].id)



@app.route('/SparkIdeaRegister', methods=['GET', 'POST'])
def SparkIdeaRegister():
    if request.method == 'GET':
        print("GET SUCESSFUL")
        return render_template('register.html')
    else:
        ########################try to create the btn onClick() event for
        if request.form.get('username') is None:
            login_rl = url_for('SparkIdeaLogin')
            return redirect(login_rl)
        else:
            username = request.form.get('username')
            password = request.form.get('password')
            password2 = request.form.get('password2')
            if password != password2:
                return " Password is not same"
            else:
                print username, password
                userResult = User.query.filter(User.username == username).first()
                if userResult != None:
                    return " Account is exist"
                else:
                    user = User(username=username, password=password)
                    db.session.add(user)
                    db.session.commit()
                    userResultNew = User.query.filter(User.username == username).first()
                    session["username"] = username
                    print("Register action --------> user id : %d" % userResultNew.id)
                    login_rl = url_for('SparkIdeaLogin')
                    return redirect(login_rl)


@app.route('/SparkIdeaLogin', methods=['GET', 'POST'])
def SparkIdeaLogin():
    if request.method == 'GET':
        print("GET SUCESSFUL")
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        session["username"] = username
        userResult = User.query.filter(User.username == username).first()
        if userResult != None:
            if userResult.password == password:
                session['username'] = username
                print("Login action --------> user id : %d" % userResult.id)
                return redirect(url_for('SparkIdeaInputKeyWords'))
            return "password is wrong!"
        return "no account!"



@app.route('/SparkIdeaInputKeyWords', methods=['GET', 'POST'])
def SparkIdeaInputKeyWords():
    if request.method == 'POST':
        KeyWord = request.form.get('KeyWord')
        NewsSource = request.form.get('NewsSource')
        return RealTimeRenderDataFromDB('1',str(KeyWord), str(NewsSource))
    else:
        return render_template('inputKeyWord.html')


# i == 1000：How many seconds will this program to run
@socketio.on('client_event')
def client_msg(msg):
    i = 1
    while True:
        w = WeblogService()
        results = w.queryWeblogs()
        titleNames = results['titleNames']
        titleCounts = results['titleCounts']
        titleSum = w.TotalTitleCount()
        retMap = {'titleNames': titleNames, 'titleCounts': titleCounts, 'titleSum': titleSum};
        emit('server_response', {'data': json.dumps(retMap)})
        time.sleep(1)
        i = i + 1
        if i == 1000:
            break



@socketio.on('connect_event')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})



def SparkIdea(isLogin):
    if isLogin == '1':
        return redirect(url_for('SparkIdeaInputKeyWords'))
    else:
        return "please Login"



#how many threads can be started at same time, just try to optimize it#################################################################
def RealTimeRenderDataFromDB(isLogin,KeyWord, NewsSource):
    if isLogin == '1':
        t = threading.Thread(target = BigData_NewsSourceInput.StartMonitor,args = (KeyWord, NewsSource))
        t.start()
        return render_template('showData.html')
    else:
        return "please Login"


if __name__ == '__main__':
    socketio.run(app)










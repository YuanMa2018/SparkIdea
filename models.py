<<<<<<< HEAD
#coding:utf-8
from extensions import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)





=======
#coding:utf-8
from extensions import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)





>>>>>>> 6a9a1f8897db0d7c063476224d81cec9aa98e922

<<<<<<< HEAD
#coding:utf-8
#JSON_AS_ASCII = False
#dialect+drive://username:password@host:port/databse
import os
DIALECT = "mysql"
DRIVE = "mysqldb"
USERNAME = "root"
PASSWORD = "400450"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "db_spark_idea"
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVE,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True

=======
#coding:utf-8
#JSON_AS_ASCII = False
#dialect+drive://username:password@host:port/databse
import os
DIALECT = "mysql"
DRIVE = "mysqldb"
USERNAME = "root"
PASSWORD = "400450"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "db_spark_idea"
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVE,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True

>>>>>>> 6a9a1f8897db0d7c063476224d81cec9aa98e922
SECRET_KEY = os.urandom(24)
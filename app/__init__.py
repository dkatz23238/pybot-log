# -*- encoding: utf-8 -*-

from flask import Flask
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
import time


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['SECRET_KEY'] = "MYSECRETKEY"
app.config['CSRF_ENABLED'] = False
#PROD = db_uri = "postgres://application:application@db:5432/robotapp"
db_uri = "postgres://application:application@db:5432/pybotlog"
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)  # flask-sqlalchemy

# Create the database tables.

from models import RoboticProcessAutomation, RPALogs


db.init_app(app)

db.create_all()

# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)
# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.

manager.create_api(RoboticProcessAutomation, methods=['GET', 'POST', 'DELETE'])
manager.create_api(RPALogs, methods=['GET', 'POST', 'DELETE'])

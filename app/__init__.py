from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
api = Api(app,
       version='0.1',
       title='Api Users Bilancio Personale',
       description='api Bilancio personale',
       endpoint='api')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://amgltnjvlajofo:e3157b0001b9af3ab0bc06c7f9b1a4aae92fad3e4a97eedd964974da967eab7d@ec2-54-217-204-34.eu-west-1.compute.amazonaws.com:5432/dhei6grndbv7l'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.create_all()

from app.controllers import users

api.add_namespace(users)
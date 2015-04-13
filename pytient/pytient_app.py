# coding: utf-8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.mongoengine import MongoEngine
import datetime

app = Flask("pytient")

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db_pytient.db'
# app.config["MONGODB_SETTINGS"] = {'DB': "db_pytient"}
app.config["SECRET_KEY"] = "02Ft5re867Ghj$kl998210cfg"

db = SQLAlchemy(app)
# db = MongoEngine(app)

import views

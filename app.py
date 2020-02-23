import sys
import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import FlaskForm
# from forms import *

from flask_migrate import Migrate
from models import db, Actor, Movie, setup_db

'''
App Config
'''
app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
setup_db(app)
migrate = Migrate(app, db)

'''
Controllers
'''
@app.route('/')
def hello():
    return jsonify({
        'success': True,
        'message': 'Hello!'
    })

'''
default port:
'''
if __name__ == '__main__':
    app.run()
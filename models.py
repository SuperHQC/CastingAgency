import os
from sqlalchemy import Column, String, Integer, DateTime, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
# import babel
# import dateutil.parser

database_name = "casting_agency"
database_path = "postgres://{}/{}".format('localhost:5432', database_name)
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    # app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
Movie
'''

class Movie(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release = Column(DateTime)

    def __init__(self, title, release):
        self.title = title
        self.release = release

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(sefl):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release': self.release.strftime("%Y %B %d"),
        }

# '''
# Parser
# '''
# def format_datetime(value, format='medium'):
#   date = dateutil.parser.parse(value)
#   if format == 'full':
#       format="EEEE MMMM, d, y 'at' h:mma"
#   elif format == 'medium':
#       format="EE MM, dd, y h:mma"
#   return babel.dates.format_datetime(date, format)

'''
Actor
'''

class Actor(db.Model):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(sefl):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }

import sys
import json


from flask import Flask, request, Response, jsonify, abort
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging

from flask_cors import CORS
from flask_migrate import Migrate
from models import db, Actor, Movie, setup_db

'''
App Config
'''
app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
setup_db(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.after_request
def after_request(response):
    response.headers.add(
        'Access-Control-Allow-Headers', 'Content-Type,Authorization,true'
    )
    response.headers.add(
        'Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS'
    )
    return response

migrate = Migrate(app, db)

'''
Controllers
'''

'''
/actors
'''
@app.route('/')
def hello():
    return jsonify({
        'success': True,
        'message': 'Hello!'
    })

@app.route('/actors', methods=['GET'])
def get_actors():
    actors = [a.format() for a in Actor.query.all()]
    # print(actors)
    return jsonify({
        'success': True,
        'actors': actors,
        'total': len(actors)
    })

@app.route('/actors', methods=['POST'])
def create_actor():

    body = request.get_json()
    if not body:
        abort(422)

    new_name = body.get('name', None)
    new_age = body.get('age', None)
    new_gender = body.get('gender', None)

    if not new_name:
        abort(422)

    new_actor = Actor(
        name= new_name,
        age= new_age,
        gender= new_gender,
    )

    new_actor.insert()
    return jsonify({
        'success': True,
        'new_actor_id': new_actor.id,
    })

@app.route('/actors/<int:id>', methods=['DELETE'])
def delete_actor(id):
    actor = Actor.query.filter(Actor.id==id).one_or_none()
    if not actor:
        abort(404)
    actor.delete()
    return jsonify({
        'success': True,
        'deleted_id': id
    })

@app.route('/actors/<int:id>', methods=['PATCH'])
def update_actor(id):
    actor = Actor.query.filter(Actor.id==id).one_or_none()
    if not actor:
        abort(404)
    body = request.get_json()
    
    if not body:
        abort(422)
    new_name = body.get('name', None)
    new_age = body.get('age', None)
    new_gender = body.get('gender', None)

    if new_name is None:
        new_name = actor.name
    if new_age is None:
        new_age = actor.age
    if new_gender is None:
        new_gender = actor.gender

    actor.name = new_name
    actor.age = new_age
    actor.gender = new_gender

    actor.update()
    return jsonify({
        'success': True,
        'updated_id': id
    })

'''
/movies
'''

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = [m.format() for m in Movie.query.all()]
    return jsonify({
        'success': True,
        'movies': movies,
        'total': len(movies)
    })

@app.route('/movies', methods=['POST'])
def create_movie():

    body = request.get_json()
    if not body:
        abort(422)
    new_title = body.get('title', None)
    new_release = body.get('release', None)

    if not new_title:
        abort(422)

    new_movie = Movie(
        title= new_title,
        release= new_release
    )

    new_movie.insert()
    return jsonify({
        'success': True,
        'new_actor_id': new_movie.id,
    })

@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.filter(Movie.id==id).one_or_none()
    if not movie:
        abort(404)
    movie.delete()
    return jsonify({
        'success': True,
        'deleted_id': id
    })

@app.route('/movies/<int:id>', methods=['PATCH'])
def update_moive(id):
    movie = Movie.query.filter(Movie.id==id).one_or_none()
    if not movie:
        abort(404)
    body = request.get_json()
    
    if not body:
        abort(422)
    new_title = body.get('title', None)
    new_release = body.get('release', None)

    if new_title is None:
        new_title = movie.title
    if new_release is None:
        new_release = movie.release

    movie.title = new_title
    movie.release = new_release
    movie.update()
    return jsonify({
        'success': True,
        'updated_id': id
    })


'''
error handlers
'''
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource Not Found"
    }), 404

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable"
    }), 422



'''
default port:
'''
if __name__ == '__main__':
    app.run()
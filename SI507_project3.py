import os
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = true
app.use_reloader = true
app.config['SECRET_KEY'] = 'asdadafaads'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sample_movies.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy

# Setting up models

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(64))
    mpaa = db.Column(db.String(10))
    imdb = db.Column(db.String(10))
    genre = db.Column(db.String(64))
    director_id = db.Column(db.String(64), db.ForeignKey('directors.id'))
    distributor_id = db.Column(db.String(64),db.ForeignKey('distributors.id'))

    def __repr__(self):
        return "{} | {}".format(self.title,self.mpaa)

class Director:
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    dob = db.Column(db.Date)
    dod = db.Column(db.Date)
    home = db.Column(db.String(64))
    movies = db.relationship('Movie',backref='Director')

    # one many
    def __repr__(self):
        return "{} from {}".format(self.name,self.home)

class MajorGenre:
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(64))

    def __repr__(self):
        return (genre)

class Distributor:
    __tablename__: 'distributors'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    movies = db.relationship('Movie',backref='Distributor')

    def __repr__(self):
        return (name)


# Helper Functions
def movie_count(data):
    return len(data)

def get_or_create_director(director_name):
    director = Director.query.filder_by(name=director_name).first()
    if director:
        return director
    else:
        director = Director(name=director_name)
        session.add(director)
        session.commit()
        return director


# Setting up Controllers
@app.route('/')
def index():
    movies = Movie.query.all()
    num_movies = len(movies)
    return render_template('index.html',num_songs) # create template

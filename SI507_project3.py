import os
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = true
app.use_reloader = true
app.config['SECRET_KEY'] = 'asdadafaads'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sample_songs.db' # TODO: decide what your new database name will be -- that has to go here
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
    movie_director = Column(db.String(64), ForeignKey('Directors.id'))
    movie_distributor = Column(db.String(64))
    director = relationship('directors')
    distributor = relationship('distributors')

    def __repr__(self):
        return "{} | {}".format(self.title,self.mpaa)

class Director:
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    dob = db.Column(db.Date)
    dod = db.Column(db.Date)
    home = db.Column(db.String(64))

    # one many
    def __repr__(self):
        return "{} from {}".format(self.name,self.home)

class MajorGenre:
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(64))

class Distributor:
    __tablename__: 'distributors'
    id
    name
    #one-many
    pass


def movie_count(data):
    return len(data)

def get_or_create_artist(artist_name):
    artist = Artist.query.filter_by(name=artist_name).first()
    if artist:
        return artist
    else:
        artist = Artist(name=artist_name)
        session.add(artist)
        session.commit()
        return artist

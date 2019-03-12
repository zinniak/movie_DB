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


class Movie:
    __tablename__ = 'movies'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(64))
    imdb = db.Column(db.String(10))
    # songs = db.relationship('')

    def __init__(self,row):
        self.title = row[1]
        self.mrating = row[7]
        self.distributor = row[9]
        self.genre = row[11]
        self.director = row[13]
        self.imdb = row[15]

    def __repr__(self):
        return "{} | {}".format(self.title,self.imdb)

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

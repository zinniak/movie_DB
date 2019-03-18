import os
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'asdadafaads'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sample_movies.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy

##### Setting up models #####

class Director(db.Model):
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    dob = db.Column(db.String(10))
    dod = db.Column(db.String(10))
    home = db.Column(db.String(64))
    movies = db.relationship('Movie',backref='Director')

    def __repr__(self):
        return "{} from {}".format(self.name,self.home)

class Genre(db.Model):
    __tablename__ = "genres"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    movies = db.relationship('Movie',backref='Genre')

    def __repr__(self):
        return genre

class Distributor(db.Model):
    __tablename__= "distributors"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    movies = db.relationship('Movie',backref='Distributor')

    def __repr__(self):
        return name

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(64))
    mpaa = db.Column(db.String(10))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))
    distributor_id = db.Column(db.Integer,db.ForeignKey('distributors.id'))

    def __repr__(self):
        return "{} | {}".format(self.title,self.mpaa)

##### Helper Functions####

def get_or_create_director(name, home='', dob='', dod=''):
    director = Director.query.filter_by(name=name).first()
    if director:
        return director

    else:
        director = Director(name=name,home=home,dob=dob,dod=dod)
        session.add(director)
        session.commit()
        return director

def get_or_create_genre(genre_name):
    genre = Genre.query.filter_by(name=genre_name).first()
    if genre:
        return genre
    else:
        genre = Genre(name=genre_name)
        session.add(genre)
        session.commit()
        return genre

def get_or_create_distributor(distributor_name):
    name = Distributor.query.filter_by(name=distributor_name).first()
    if name:
        return name
    else:
        name = Distributor(name=distributor_name)
        session.add(name)
        session.commit()
        return name

##### Setting up controllers #####

# route for home page
@app.route('/')
def index():
    movies = Movie.query.all()
    num_movies = len(movies)
    return render_template('index.html',num_movies=num_movies) # create template

# route to create new director
@app.route('/new/director/<name>/<home>/<dob>/<dod>')
def new_director(name,home,dob,dod):
    if Director.query.filter_by(name=name).first():
        return "This Director already exists in the database. Please go back to the home page"
    else:
        director = get_or_create_director(name,home=home,dob=dob,dod=dod)
        return "New Director added: {} from {}".format(director.name,director.home)

# route to create new genre
@app.route('/new/genre/<name>')
def new_genre(name):
    if Genre.query.filter_by(name=name).first():
        return "This Genre already exists in the database. Please go back to the home page"
    else:
        genre = get_or_create_genre(name)
        return "New Genre added: {}".format(genre.name)

#route to create new distributor
@app.route('/new/distributor/<name>')
def new_distributor(name):
    if Distributor.query.filter_by(name=name).first():
        return "This Distributor already exists in the database. Please go back to the home page"
    else:
        distributor = get_or_create_distributor(name)
        return "New Distributor added: {}".format(distributor.name)

# route to create new movie
@app.route('/new/movie/<title>/<mpaa>/<genre>/<director>/<distributor>')
def new_movie(title,mpaa,genre,director,distributor):
    if Movie.query.filter_by(title=title).first():
        return "This Movie already exists in the database. Please go back to the home page"
    else:
        director = get_or_create_director(director)
        genre = get_or_create_genre(genre)
        distributor = get_or_create_distributor(distributor)
        movie = Movie(title=title,mpaa= mpaa,director_id=director.id,genre_id=genre.id,distributor_id=distributor.id)
        session.add(movie)
        session.commit()
        return "New {} rated movie: {}".format(movie.mpaa,movie.title)

# route to get a list of all movies
@app.route('/all_movies')
def see_all_movies():
    all_movies = []
    movies = Movie.query.all()
    for m in movies:
        genre = Genre.query.filter_by(id=m.genre_id).first()
        director = Director.query.filter_by(id=m.director_id).first()
        distributor = Distributor.query.filter_by(id=m.distributor_id).first()
        all_movies.append((m.title,m.mpaa,genre.name,director.name,distributor.name))
    return render_template('all_movies.html',all_movies=all_movies)

if __name__ == '__main__':
    db.create_all()
    app.run()

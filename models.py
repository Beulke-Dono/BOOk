from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

class Author(db.Model):
    __tablename__ = 'Author'
    id_author = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('User.id_user'), nullable=False)
    name_author = db.Column(db.String(100), nullable=False)

class Book(db.Model):
    __tablename__ = 'Book'
    id_book = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    overview = db.Column(db.String(500), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    cover_image = db.Column(db.String(100), nullable=False)

class Genre(db.Model):
    __tablename__ = 'Genre'
    id_genre = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_genre = db.Column(db.String(100), nullable=False)

class Book_Genre(db.Model):
    __tablename__ = 'Book_Genre'
    id_book = db.Column(db.Integer, db.ForeignKey('Book.id_book'), primary_key=True)
    id_genre = db.Column(db.Integer, db.ForeignKey('Genre.id_genre'), primary_key=True)

class Book_Author(db.Model):
    __tablename__ = 'Book_Author'
    id_book = db.Column(db.Integer, db.ForeignKey('Book.id_book'), primary_key=True)
    id_author = db.Column(db.Integer, db.ForeignKey('Author.id_author'), primary_key=True)

class SavedBooks(db.Model):
    __tablename__ = 'SavedBooks'
    id_user = db.Column(db.Integer, db.ForeignKey('User.id_user'), primary_key=True)
    id_book = db.Column(db.Integer, db.ForeignKey('Book.id_book'), primary_key=True)
    saved_date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

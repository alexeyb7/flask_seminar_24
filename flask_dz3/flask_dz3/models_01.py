import nullable
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    bookname = db.Column(db.String(50), nullable = False)
    publicyear = db.Column(db.Integer, nullable = False)
    copies = db.Column(db.Integer, nullable = False)
    id_author = db.Column(db.Integer, db.ForeignKey('author.id'), nullable = False)

    def __repr__(self):
        return f'Книга:{self.bookname}, Автор:{self.id_author}'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(30), nullable = False)
    lastname = db.Column(db.String(30), nullable = False)

    def __repr__(self):
        return f'Автор{self.firstname} {self.lastname}'

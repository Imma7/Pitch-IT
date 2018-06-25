from . import db

    #User class
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(10))
    pitches = db.relationship('Pitch', backref = 'user', lazy = "dynamic")
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    comment = db.Column(db.String)
    category = db.Column(db.String)
    vote = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'pitches', lazy = "dynamic")
    votes = db.relationship('Vote', backref = 'pitches', lazy = "dynamic")

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key = True)
    category_name = db.Column(db.String)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    feedback = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    votes = db.relationship('Vote', backref = 'comments', lazy = "dynamic")
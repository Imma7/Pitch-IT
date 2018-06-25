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


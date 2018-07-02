from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#User class
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref = 'user', lazy = "dynamic")
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(100))
    photoprofiles = db.relationship('PhotoProfile', backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

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

class Vote(db.Model):
    __tablename__ = 'votes'
    id = db.Column(db.Integer, primary_key = True)
    vote = db.Column(db.Integer)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))

class PhotoProfile(db.Model):
    __tablename__ = 'photoprofiles'
    id = db.Column(db.Integer, primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
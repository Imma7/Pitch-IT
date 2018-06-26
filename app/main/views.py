from flask import render_template,request,redirect,url_for
from . import main
from ..models import User, Pitch, Category, Vote, Comment
from flask_login import login_required

#Views
@main.route('/')
@login_required
def index():
    '''
    '''
    pass

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
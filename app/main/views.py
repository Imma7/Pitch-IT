from flask import render_template,request,redirect,url_for
from . import main
from ..models import User, Pitch, Category, Vote, Comment
from flask_login import login_required
from .forms import UpdateProfile

#Views
@main.route('/')
@login_required
def index():
    '''
    '''
    pass

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))

    return render_template("profile/profile.html", user = user)
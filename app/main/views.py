from flask import render_template,request,redirect,url_for
from . import main
from ..models import User, Pitch, Category, Vote, Comment
from flask_login import login_required
from .forms import UpdateProfile, PitchForm, CommentForm, CategoryForm
from .. import db, photos

#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # form = PitchForm()
    category = Category.get_categories()


    return render_template('index.html',  category = category)

@main.route('/add/category', methods=['GET','POST'])
@login_required
def new_category():
    '''
    View new group route function that returns a page with a form to create a category
    '''
    form = CategoryForm()

    if form.validate_on_submit():
        name = form.name.data
        new_category = Category(category_name=name)
        new_category.save_category()

        return redirect(url_for('.new_category'))

    all_categories = Category.query.order_by('-id').all()
    title = 'New category'
    return render_template('new_category.html', category_form = form,title=title, categories = all_categories )


@main.route('/user/<uname>/update/pic', methods = ['POST'])
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

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

    return render_template("profile/profile.html", user = user)
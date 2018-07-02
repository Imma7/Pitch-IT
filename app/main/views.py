from flask import render_template,request,redirect,url_for, abort
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
        new_category = Category(name=name)
        new_category.save_category()

        return redirect(url_for('.index'))

    
    title = 'New category'
    return render_template('new_category.html', category_form = form,title=title)

@main.route('/categories/<int:id>')
def category(id):
    category = Pitch.query.get(id)
    if category is None:
        abort(404)

    pitches=Pitch.get_pitches(id)
    title = f'{category.name} page'
    return render_template('category.html', pitches=pitches, category=category)

#Route for adding a new pitch
@main.route('/category/new-pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def new_pitch(id):
    '''
    Function to check Pitches form and fetch data from the fields
    '''
    form = PitchForm()
    category = PitchCategory.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    if form.validate_on_submit():
        content = form.content.data
        new_pitch= Pitch(content=content,category_id= category.id,user_id=current_user.id)
        new_pitch.save_pitch()
        return redirect(url_for('.category', id=category.id))

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
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
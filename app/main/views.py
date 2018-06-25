from flask import render_template,request,redirect,url_for
from . import main
from ..models import Movie, Review
#Views
@main.route('/')
def index():
    '''
    '''
    pass
from flask import render_template,request,redirect,url_for
from . import main
from ..models import User, Pitch, Category, Comment, Vote

#Views
@main.route('/')
def index():
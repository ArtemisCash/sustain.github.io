from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/sign-up')
def signup():
    return render_template('sign-up.html')

@auth.route('/login')
def login():
    return render_template('login.html')
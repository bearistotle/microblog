from flask import render_template, flash, redirect, request, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, login_required
from app.models import User
from werkzeug.urls import url_parse

# define view for index page (both decorators linked to f(x) below)
@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Brandon'}
    posts = [
        {
            'author': {'username': 'Car'},
            'image': 'app/images/thinking-panda.jpg',
            'body': 'Beautiul day in Philly!'
        },
        {
            'author': {'username': 'Brandon'},
            'image': 'images/ponderbear.jpg',
            'body': 'Leave me alone and let me code...'
        },
        {
            'author': {'username': 'Jake'},
            'image': 'images/thinking-polar.jpg',
            'body': "I'm just not gonna eat for a week."
        },
        {
            'author': {'username': 'Jordan'},
            'image': 'images/thinking-sun.jpg',
            'body': "Why is the theme bears? Sharks and octopi are way cooler!"
        }
    ]
    return render_template('index.html', title="Home", posts=posts)

# define view for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect('/' + next_page)
    return render_template('login.html', title='Sign In', form=form)

# define view for about page
@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

# define view for index page (both decorators linked to f(x) below)
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Brandon'}
    posts = [
        {
            'author': {'username': 'Jim'},
            'body': 'Beautiul day in Philly!'
        },
        {
            'author': {'username': 'Dwight'},
            'body': 'The Avengers movie was awesome!'
        },
        {
            'author': {'username': 'Toby'},
            'body': 'My latest Chad Flenderman novel is now on Amazon!'
        },
        {
            'author': {'username': 'Michael'},
            'body': "Ugh, Toby, nobody cares!---Hey, anybody know where Ryan is? He isn't answering my calls..."
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)

# define view for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

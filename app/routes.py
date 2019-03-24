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
            'author': {'username': 'Car'},
            'image': 'https://i.pinimg.com/474x/83/06/74/830674470a92d1e739b1123a85a727e9.jpg',
            'body': 'Beautiul day in Philly!'
        },
        {
            'author': {'username': 'Brandon'},
            'image': 'https://twistedsifter.files.wordpress.com/2014/01/bearistotle-thinking-bear.jpg?w=300',
            'body': 'Leave me alone and let me code...'
        },
        {
            'author': {'username': 'Jake'},
            'image': 'https://images.ecosia.org/b2q8xy25isChnGRztjSfBR3I0xk=/0x390/smart/http%3A%2F%2F3.bp.blogspot.com%2F-L1UpkrgK7LE%2FTkxMNtkPE3I%2FAAAAAAAABg8%2FLsiokoBHme8%2Fs1600%2Fhumorous%2Bhilarious%2Bfunny%2Bpictures%2Bof%2Banimals_Polar_Bear.jpg',
            'body': "I'm just not gonna eat for a week."
        },
        {
            'author': {'username': 'Jordan'},
            'image': 'https://images.ecosia.org/8RhGD26cmeiqbckHvYK--4roQd0=/0x390/smart/https%3A%2F%2Fi.pinimg.com%2F236x%2Fba%2Fb1%2F6f%2Fbab16f6102d4867096bd8e9c1a21e5cc.jpg',
            'body': "Why is the theme bears? Sharks and octopi are way cooler!"
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
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

# define view for about page
@app.route('/about')
def about():
    return render_template('about.html', title='About')

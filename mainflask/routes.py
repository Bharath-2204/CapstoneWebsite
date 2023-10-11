from flask import render_template , url_for ,flash, redirect
from mainflask.forms import RegistrationForm, LoginForm
from mainflask import app, db, bcrypt
from mainflask.models import User, Post

    
posts=[
    {
        "author": "gowri",
        "title":"ADHD",
        "content":"yeah"
    },
    {
        "author":"aryan",
        "title":"yeah",
        "content":"okay"
    }]

@app.route("/")
def default():
    return "<h1> this is the default page no</h1>"
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)


@app.route("/about")
def about():
    return render_template("about.html" , title="About")

@app.route("/questionnaire")
def questionnaire():
    return render_template("questionnaire.html" , title="Questionnaire")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():  
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

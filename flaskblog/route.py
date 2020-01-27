from flask import  render_template, url_for , flash , redirect
from flaskblog import app ,db,bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


posts =[
    {
        'author' : 'Sotunbo David',
        'title' : 'Blog Post 1',
        'content' : 'First Post Content',
        'date_posted' : ' January 4, 2020'
    },
    {
        'author' : 'Sotunbo David',
        'title' : 'Blog Post 2',
        'content' : 'Second Post Content',
        'date_posted' : ' January 7, 2020'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts= posts)

@app.route("/about")
def about():
    return render_template('about.html', title = "About")

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations !! Your account has been succesfully created and you are in .Welcome !', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods=['GET', "POST"])
def login():
    form = LoginForm()
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
        flash('You have been logged in sucessfully', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login Unsuceesfull. Please check username and password', 'danger')
    return render_template('login.html', title = 'Login', form = form)
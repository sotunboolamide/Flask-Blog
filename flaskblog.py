from flask import Flask, render_template, url_for , flash , redirect
from forms import RegistrationForm, LoginForm
app= Flask(__name__)

app.config['SECRET_KEY'] = 'd5c8bc8a808acef6421d75ba0621204300e4d8961e8aa33b4e'
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
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)

if __name__== '__main__':
    app.run(debug=True)
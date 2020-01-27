from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app= Flask(__name__)
app.config['SECRET_KEY'] = 'd5c8bc8a808acef6421d75ba0621204300e4d8961e8aa33b4e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import route
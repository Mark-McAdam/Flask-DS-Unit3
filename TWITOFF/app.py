""" Code for the app
import Flask
make the application
make the routes 
"""

from flask import Flask
from .models import db

#make app factory - reference the app.py file and the function inside
def create_app():
    app = Flask(__name__)

    #add config for the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    #initialize database for the app - move to postgresql for the final format
    db.init_app(app)


    @app.route('/')
    def root():
        return "welcome to twitoff"
    return app
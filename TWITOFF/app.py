""" Code for the app
import Flask
make the application
make the routes 
"""

from flask import Flask

# make app factory - reference the app.py file and the function inside
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return "welcome to twitoff"
    return app
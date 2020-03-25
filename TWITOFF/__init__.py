""" Entry Point for Twitoff App""" 

from .app import create_app

APP = create_app()

SQLALCHEMY_TRACK_MODIFICATIONS = False

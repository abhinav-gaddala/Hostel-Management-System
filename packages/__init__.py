from flask import Flask, render_template
# from .auth import auth
# from . import db
import urllib.parse as urlparse
import os

# URL =  urlparse.urlparse(os.environ['DATABASE_URL'])
# DEBUG = True
# SECRET_KEY = 'sathwikisgreat'


def create_app():
    app = Flask(__name__)
    # app.config.from_object(__name__)
    # app.register_blueprint(auth, url_prefix='/')
    # db.init_app(app)
    return app
"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from flask import Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:live@localhost/finalproject'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:RenVenrascal@localhost/finalproj'
 
from models import db
db.init_app(app)

import intro_to_flask.main
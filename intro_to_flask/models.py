from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Officer(db.Model):
  __tablename__ = 'officer'
  userid = db.Column(db.Integer, primary_key = True)
  email_address = db.Column(db.String(100), unique=True)
  passcode=db.Column(db.String(100))
  role =db.Column(db.String(100))
  division= db.Column(db.String(100))
  station=db.Column(db.String(100))
  name =db.Column(db.String(100))
  
   
  def __init__(self, name, email, passcode):
    self.name = name.title()
    self.email = email.lower()
    self.set_password(passcode)
     
  def set_password(self, pword):
    self.passcode = generate_password_hash(pword)
   
  def check_password(self, pword):
    return check_password_hash(self.passcode, pword)
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash


db = SQLAlchemy()

class Officer(db.Model):
    __tablename__ = 'officer'
    userid = db.Column(db.INT, autoincrement=True, unique=True, primary_key = True)
    email_address = db.Column(db.VARCHAR(255), unique=True)
    password=db.Column(db.VARCHAR(255))
    role =db.Column(db.VARCHAR(255))
    division= db.Column(db.VARCHAR(255))
    station=db.Column(db.VARCHAR(255))
    name =db.Column(db.VARCHAR(255))
  
   
    def __init__(self, name, email, passcode):
        self.name = name.title()
        self.email = email.lower()
        self.set_password(passcode)
     
    def set_password(self, pword):
        self.passcode = generate_password_hash(pword)
     
    def check_password(self, pword):
        return check_password_hash(self.passcode, pword)
    
class Profile(db.Model):
    __tablename__= 'profile'
    profileid = db.Column(db.INT, nullable=False, unique=True, autoincrement=True , primary_key=True)
    picture = db.Column(db.BLOB)
    home_address = db.Column(db.VARCHAR(255))
    gender = db.Column(db.VARCHAR(255))
    first_name = db.Column(db.VARCHAR(255))
    middle_name = db.Column(db.VARCHAR(255))
    last_name  = db.Column(db.VARCHAR(255))
    weapon_of_choice = db.Column(db.VARCHAR(255))
    height = db.Column(db.NUMERIC(4,2))
    weight = db.Column(db.NUMERIC(6,2))
    build = db.Column(db.VARCHAR(255))
    complexion = db.Column(db.VARCHAR(255))
    hair_colour = db.Column(db.VARCHAR(255))
    eye_colour = db.Column(db.VARCHAR(255))
    ethnicity = db.Column(db.VARCHAR(255))
    scars = db.Column(db.VARCHAR(255))
    work_address = db.Column(db.VARCHAR(255))
    work_contact_no = db.Column(db.VARCHAR(255))
    job_title  = db.Column(db.VARCHAR(255)) 
    mother_first_name = db.Column(db.VARCHAR(255))
    mother_maiden_name = db.Column(db.VARCHAR(255))
    mother_surname = db.Column(db.VARCHAR(255))
    mother_address = db.Column(db.VARCHAR(255))
    mother_nationality = db.Column(db.VARCHAR(255))
    father_first_name = db.Column(db.VARCHAR(255))
    father_surname = db.Column(db.VARCHAR(255))
    father_address = db.Column(db.VARCHAR(255))
    father_nationality = db.Column(db.VARCHAR(255))
    date_create = db.Column(db.DATETIME)
    
    def __init__(self, profileid,picture,home_address,gender,first_name ,middle_name,last_name,weapon_of_choice ,height,weight,build,complexion
    ,hair_colour 
    ,eye_colour 
    ,ethnicity 
    ,scars 
    ,work_address 
    ,work_contact_no
    ,job_title 
    ,mother_first_name 
    ,mother_maiden_name
    ,mother_surname 
    ,mother_address
    ,mother_nationality 
    ,father_first_name
    ,father_surname 
    ,father_address
    ,father_nationality
    ,date_create):
        self.profileid =profileid
        self.picture=picture 
        self.home_address=home_addres
        self.gender =gender 
        self.first_name =first_name 
        self.middle_name=middle_name
        self.last_name  =last_name  
        self.weapon_of_choice =weapon_of_choice 
        self.height =height 
        self.weight=weight
        self.build=build
        self.complexion=complexion
        self.hair_colour =hair_colour 
        self.eye_colour=eye_colour  
        self.ethnicity =ethnicity 
        self.scars =scars 
        self.work_address =work_address 
        self.work_contact_no=work_contact_no
        self.job_title =job_title 
        self.mother_first_name =mother_first_name 
        self.mother_maiden_name=mother_maiden_name
        self.mother_surname =mother_surname 
        self.mother_address=mother_address
        self.mother_nationality =mother_nationality 
        self.father_first_name=father_first_name
        self.father_surname=father_surname  
        self.father_address=father_address
        self.father_nationality=father_nationality
        self.date_create=date_create
        
    def __repr__(self):
        return '<User %r>' % self.useridref
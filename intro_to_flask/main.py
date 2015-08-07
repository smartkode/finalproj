"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from intro_to_flask import app
from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from models import db, Officer
from forms import ContactForm, ProfileForm, ReportForm, SignupForm, LoginForm
from flask_mail import Message, Mail

from flask.ext.mysqldb import MySQL

mail = Mail(app)

app.config['SECRET_KEY'] = '!q76$@8(8sdscjksfcbrvy; %$#'
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'cmclaren89@gmail.com'
app.config["MAIL_PASSWORD"] = 'wwhiimwvcrbnenpt'

mail.init_app(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'RenVenrascal'
app.config['MYSQL_DB'] = 'finalproj'

# mysql = MySQL(app)

# --  Test database  --------------------------------------------------------------------------------------------------------------------------
@app.route('/testdb/')
def testdb():
    if db.session.query("1").from_statement("SELECT 1").all():
	return 'it works'
    else:
	return 'something is broke'


# --  Home Page  -------------------------------------------------------------------------------------------------------------------------------
@app.route('/', methods=['GET'])
def home():
    
    return render_template('home.html')
    
# --  About Page  -------------------------------------------------------------------------------------------------------------------------------
@app.route('/about/', methods=['GET'])
def about(name=None):
    
    return render_template('about.html', name=name)

# --  View Profiles  ----------------------------------------------------------------------------------------------------------------------------
@app.route('/profile/', methods=['GET', 'POST'])
def profile(name=None):
    
    return render_template('profile.html', name=name)

# --  View Reports  ------------------------------------------------------------------------------------------------------------------------------
@app.route('/report/')
def report(name=None):
    """Render the website's about page."""
    return render_template('report.html',name=name)

    
# --  User Feedback  -----------------------------------------------------------------------------------------------------------------------------    
@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender=request.form['email'], recipients=['cmclaren89@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return 'Form posted.'

    elif request.method == 'GET':
        return render_template('contact.html', form=form)

# --  Input Forms  -------------------------------------------------------------------------------------------------------------------------------
@app.route('/forms/')
def forms():
    return render_template('forms.html')

@app.route('/profile/edit/', methods=['GET', 'POST'])
def profileedit():
    form = ProfileForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('profileedit.html', form=form)
        else:
            profile = Profile(form.picture,form.home_address,form.gender,form.first_name ,form.middle_name,form.last_name,form.weapon_of_choice ,form.height,form.weight,form.build,form.complexion,form.hair_colour ,form.eye_colour ,form.ethnicity ,form.scars ,form.work_address ,form.work_contact_no,form.job_title ,form.mother_first_name ,form.mother_maiden_name,form.mother_surname,form.mother_address,form.mother_nationality,form.father_first_name,form.father_surname ,form.father_address,form.father_nationality,form.date_create)
            db.session.add(profile)
            db.session.commit()
            return 'Form posted.'

    elif request.method == 'GET':
        return render_template('profileedit.html', form=form)
    
@app.route('/report/edit/', methods=['GET', 'POST'])
def reportedit():
    form = ReportForm()

    if request.method == 'POST':
        return 'Form posted.'

    elif request.method == 'GET':
        return render_template('reportedit.html', form=form)

# --  Site Login  --------------------------------------------------------------------------------------------------------------------------------
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('login.html', form=form)
    return render_template('login.html',form=form)
    #



@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
   
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('signup.html', form=form)
        else:
            new_officer = Officer(form.firstname.data, form.lastname.data, form.email_address.data, form.password.data)
            db.session.add(new_officer)
            db.session.commit()
        return "[1] Create a new user [2] sign in the user [3] redirect to the user's profile"
    elif request.method == 'GET':
        return render_template('signup.html', form=form)
 ###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404




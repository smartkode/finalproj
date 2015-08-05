"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from intro_to_flask import app
from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from models import db
from forms import ContactForm, ProfileForm, ReportForm
from flask_mail import Message, Mail


#from flask.ext.mysqldb import MySQL
#app = Flask(__name__)
mail = Mail(app)


app.config['SECRET_KEY'] = '!q76$@8(8sdscjksfcbrvy; %$#'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'cmclaren89@gmail.com'
app.config["MAIL_PASSWORD"] = 'wwhiimwvcrbnenpt'
# app.config['MAIL_DEBUG'] = True
# app.config['MAIL_SUPPRESS_SEND'] = False
# app.config['MAIL_MAILER'] = '/usr/sbin/sendmail'
# app.config['MAIL_FAIL_SILENTLY'] = False

mail.init_app(app)


#mysql = MySQL(app)

@app.route('/testdb/')
def testdb():
    if db.session.query("1").from_statement("SELECT 1").all():
	return 'it works'
    else:
	return 'something is broke'

#if __name__ == '__main__':
#    app.run(debug=True)
###
# Routing for your application.
###

@app.route('/', methods=['GET'])
def home(name=None):
    """Render the website's home page."""
    return render_template('home2.html', name=name)
    

@app.route('/about/', methods=['GET'])
def about(name=None):
    """Render the website's about page."""
    return render_template('about.html', name=name)

@app.route('/profile/', methods=['GET', 'POST'])
def profile(name=None):
    """Render the website's profile page."""
    return render_template('profile.html', name=name)
    
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



@app.route('/profile/edit/', methods=['GET', 'POST'])
def profileedit():
    form = ProfileForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            return 'Form posted.'

    elif request.method == 'GET':
        return render_template('profileedit2.html', form=form)
    


@app.route('/login/')
def login(name=None):
    """Render the website's login page."""
    return render_template('login.html',name=name)
    #
@app.route('/report/')
def report(name=None):
    """Render the website's about page."""
    return render_template('report.html',name=name)

@app.route('/report/edit/', methods=['GET', 'POST'])
def reportedit():
    form = ReportForm()

    if request.method == 'POST':
        return 'Form posted.'

    elif request.method == 'GET':
        return render_template('reportedit2.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      new_officer = Officer(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
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




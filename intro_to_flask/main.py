"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from intro_to_flask import app
from flask import Flask
from flask import render_template, request, redirect, url_for
from models import db

#from flask.ext.mysqldb import MySQL
#app = Flask(__name__)


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

@app.route('/')
def home(name=None):
    """Render the website's home page."""
    return render_template('home2.html',name=name)
    

@app.route('/about/')
def about(name=None):
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile/')
def profile(name=None):
    """Render the website's profile page."""
    return render_template('profile.html',name=name)
    
@app.route('/contact/')
def contact(name=None):
    """Render the website's contact page."""
    return render_template('contact.html',name=name)



@app.route('/profile/edit/')
def profileedit(name=None):
    """Render the website's edit profile page."""
    return render_template('profileedit.html',name=name)
    


@app.route('/login/')
def login(name=None):
    """Render the website's login page."""
    return render_template('login.html',name=name)
    #
@app.route('/report/')
def report(name=None):
    """Render the website's about page."""
    return render_template('report.html',name=name)

@app.route('/report/edit/')
def reportadd(name=None):
    """Render the website's about page."""
    return render_template('reportedit.html',name=name)

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



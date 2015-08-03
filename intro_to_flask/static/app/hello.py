
# Importing the Flask Framework
from flask import Flask
from flask import render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html') #'Hello tks World!'

if __name__ == '__main__':
    app.run(debug=True)
    


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

    
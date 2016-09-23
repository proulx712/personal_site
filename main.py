# [START app]
import logging

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_home():
    return render_template('pages/home.html')


@app.route('/resume', methods=['GET'])
def get_resume():
    return render_template('pages/resume.html')


@app.route('/contact', methods=['GET'])
def get_contact():
    return render_template('pages/contact.html')


@app.route('/about', methods=['GET'])
def get_about():
    return render_template('pages/about.html')


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return render_template('505.html'), 500
    # [END app]

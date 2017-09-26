# [START app]
import logging

from flask import Flask, render_template
from flask import send_file

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_home():
    return render_template('base.html')


@app.route('/download', methods=['POST'])
def download_resume():
    return send_file('docs/PROULX_RESUME.pdf', as_attachment=True)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return render_template('505.html'), 500
    # [END app]

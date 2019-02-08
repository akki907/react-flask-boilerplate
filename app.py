import os
import sys
from flask import Flask ,session, redirect, url_for, escape, request,send_from_directory,render_template
from flask_cors import CORS
app = Flask(__name__, static_folder="./frontend/build/static", template_folder="./frontend/build")

CORS(app)




@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    # LOG.info('running environment: %s', os.environ.get('ENV'))
    app.config['DEBUG'] = os.environ.get('ENV') == 'development' # Debug mode if development env
    app.run() # Run the app
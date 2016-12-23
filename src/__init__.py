# Import required libraries
from flask import Flask, render_template
from pony.orm import *
from ConfigParser import SafeConfigParser

# Create the configuration of the app
conf = SafeConfigParser()
conf.read('src/config.ini')

# Create the flask application to run
app = Flask(__name__)

# Make the configuration object available in templates
app.jinja_env.globals.update(conf=conf)

# Configure the database
db = Database()
db.bind('mysql', host=conf.get('db', 'host'), db=conf.get('db', 'db'), user=conf.get('db', 'user'), passwd=conf.get('db', 'passwd'))

# Add error handlers to default pages so there is no fuzz
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404
@app.errorhandler(403)
def forbidden(e):
    return render_template('error/403.html'), 403
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error/500.html'), 500

# Load the models and routes of the application
import src.models
import src.routes

db.generate_mapping(create_tables=True)

app.run(host='0.0.0.0', port=conf.get('app', 'port'))

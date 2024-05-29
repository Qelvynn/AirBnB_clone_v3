#!/usr/bin/python3
"""
Flask Application for AirBnB clone API

This module initializes the Flask application and sets up CORS, Swagger,
and other configurations necessary for the AirBnB clone Restful API.
It includes error handling and teardown logic to manage resources efficiently.
"""

# Importing necessary libraries and modules
from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

# Initialize Flask application
app = Flask(__name__)
# Enable pretty print for JSON responses
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# Register blueprints for app_views
app.register_blueprint(app_views)
# Set up CORS with wildcard origin
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

@app.teardown_appcontext
def close_db(error):
    """
    Close the database session at the end of the request or when the application shuts down.
    
    Args:
        error: The error object passed to the teardown function.
    """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """
    Error handler for 404 errors that returns a JSON-formatted 404 response.
    
    Args:
        error: The error object passed to the error handler.
    
    Returns:
        A Flask response object with a JSON payload containing the error message.
    """
    return make_response(jsonify({'error': "Not found"}), 404)

# Swagger configuration
app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}
# Initialize Swagger
Swagger(app)

if __name__ == "__main__":
    """
    Main function to run the Flask application.
    
    Retrieves the host and port from the environment variables with default fallbacks.
    Starts the Flask application with the specified host, port, and threading enabled.
    """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)

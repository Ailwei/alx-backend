#!/usr/bin/env python3
"""A simple Flask app."""

from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    """Configuration class for the Flask app."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

# Configure the Flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Determine the best-matching language for the user."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Render the index template."""
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)

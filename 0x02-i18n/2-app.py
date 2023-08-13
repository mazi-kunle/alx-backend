#!/usr/bin/env python3
'''This is a flask module'''


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''config class'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
# print(app.config)


@app.route('/')
def hello_world():
    '''
    render a simple hello world page
    '''
    return render_template('0-index.html')


@babel.localeselector
def get_locale():
    '''get best locale'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()

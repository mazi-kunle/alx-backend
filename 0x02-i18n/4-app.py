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
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    '''get best locale'''
    if (request.args.get('locale') in ['fr', 'en']):
        return request.args.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel = Babel(app, locale_selector=get_locale)

if __name__ == '__main__':
    app.run()

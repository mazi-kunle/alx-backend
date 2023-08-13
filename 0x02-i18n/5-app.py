#!/usr/bin/env python3
'''This is a flask module'''


from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''config class'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@app.route('/')
def hello_world():
    '''
    render a simple hello world page
    '''
    return render_template('5-index.html', user=g.user)


@babel.localeselector
def get_locale():
    '''get best locale'''
    if (request.args.get('locale') in ['fr', 'en']):
        return request.args.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    '''mock login'''
    login_details = int(request.args.get('login_as'))
    if (login_details is not None and login_details in users):
        return users.get(int(login_details))

    return None


@app.before_request
def before_request():
    '''get user of exists and set as global on flask.g.user'''
    g.user = get_user()


# babel = Babel(app, locale_selector=get_locale)

if __name__ == '__main__':
    app.run()

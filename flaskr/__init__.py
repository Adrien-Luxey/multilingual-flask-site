import os 

from flask import Flask, redirect, url_for
from flask.cli import AppGroup
from flask_babel import Babel

babel = Babel()
translate_cli = AppGroup('translate')

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='i-would-never-commit-my-secret-key-to-github',
        BABEL_DEFAULT_LOCALE='en',
        BABEL_TRANSLATION_DIRECTORIES=
            os.path.join(os.getcwd(), __name__, 'translations'),
        LANGUAGES = {
            'fr': 'Français 🇫🇷',
            'en': 'English 🇬🇧'
        }
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    babel.init_app(app)

    # Don't forget to import these, they contain important decorated functions
    from . import cli, locale

    app.cli.add_command(translate_cli)

    from . import errors, blueprint
    app.register_error_handler(404, errors.page_not_found)
    app.register_blueprint(blueprint.bp)

    # Where does / go? 
    # Redirect to the frontend Blueprint's static function, with page=index.
    @app.route('/')
    def index():
        return redirect(url_for( 'frontend.static', page='index' ))

    return app
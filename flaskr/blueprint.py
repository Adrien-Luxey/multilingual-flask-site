from flask import Blueprint, g, current_app, render_template

bp = Blueprint('frontend', __name__, url_prefix='/<lang_code>')

@bp.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', 
        g.get('lang_code', current_app.config['BABEL_DEFAULT_LOCALE']))

@bp.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code', current_app.config['BABEL_DEFAULT_LOCALE'])


@bp.route('/', defaults={'page': 'index'})
@bp.route('/<page>')
def static(page):
    return render_template(f'static/{page}.html')
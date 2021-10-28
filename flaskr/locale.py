from . import babel
from flask import g, current_app, request


@babel.localeselector
def get_locale():
    # Try to retrieve the language from the context
    lang_code = getattr(g, 'lang_code', None)
    if lang_code is not None:
        # print(f"get_locale: found lang_code={lang_code} in g.")
        return lang_code

    # otherwise try to guess the language from the user accept
    # header the browser transmits. The best match wins.
    accepted_langs = list(current_app.config['LANGUAGES'].keys())
    lang_code = request.accept_languages.best_match(accepted_langs)
    # print(f"get_locale: default lang_code={lang_code}")
    return 
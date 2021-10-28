"""
Code adapted from: https://github.com/hazzillrodriguez/flask-multi-language
"""

from . import translate_cli
from flask import current_app
import click
import os

@translate_cli.command()
@click.argument('lang')
def init(lang):
    """Initialize a new language."""
    if os.system('pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system(
            f'pybabel init -i messages.pot -d {current_app.name}/translations -l ' + lang):
        raise RuntimeError('init command failed')
    os.remove('messages.pot')

@translate_cli.command()
def update():
    """Update all languages."""
    if os.system('pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system(
    f'pybabel update -i messages.pot -d {current_app.name}/translations'):
        raise RuntimeError('update command failed')
    os.remove('messages.pot')

@translate_cli.command()
def compile():
    """Compile all languages."""
    if os.system(f'pybabel compile -d {current_app.name}/translations'):
        raise RuntimeError('compile command failed')
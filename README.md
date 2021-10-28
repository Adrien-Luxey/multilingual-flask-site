# Multilingual Flask site

A minimal installation of Flask and Flask-Babel, so as to propose multiple languages depending on the request URL (e.g. `/en/index` vs `/fr/index`).

## Installation

Install dependencies through `pipenv`:

```bash
pipenv install 
```

Everytime you want your Shell session to use the project's dependencies, run:

```bash
pipenv shell
```

Before running any `flask` command, do setup the required environment variables, e.g. :

```bash
export FLASK_APP=flaskr # name of the python module containing our codebase
export FLASK_ENV=development 
```

## Translations

[Flask-Babel](https://flask-babel.tkte.ch/) takes care of business---go read their docs for info.

Only note that, instead of calling `pybabel` as written in [Flask-Babel's documentation](https://flask-babel.tkte.ch/), a CLI module is installed on the site to ease things (courtesy of @hazzillrodriguez's [`flask-multi-language`](https://github.com/hazzillrodriguez/flask-multi-language)):

* To generate the translation `.po` files  files for a language, run:

	```bash
	flask translate init <language-code>
	```

* Putting `fr` as the `<language-code>`, the above would generate the file `flaskr/translations/fr/LC_MESSAGES/messages.po`. It will look like:

	```
	#: flaskr/templates/base.html:10
	msgid "Multilingual flask site"
	msgstr ""

	#: flaskr/templates/base.html:22
	msgid "Home"
	msgstr ""

	#: flaskr/templates/base.html:81
	msgid "No rights reserved"
	msgstr ""

	#: flaskr/templates/base.html:87
	msgid "Source code"
	msgstr ""
	```

	Now fill-in the French translations!

* Once you're done translating, you can generate Babel's binary output file (`.mo`):

	```bash
	flask translate compile
	```

* Next time you edit your site, only `update` translations (your existing translations will be kept):

	```bash
	flask translate update
	# Then recompile
	flask translate compile
	```


## Running locally

Simply run:

```bash
# If not already done:
pipenv shell
export FLASK_ENV=development
export FLASK_APP=flaskr
# The righteous command:
flask run
```

Then go check it out on [http://127.0.0.1:5000](http://127.0.0.1:5000) !

## Your site is so beautiful, Adrien!

Thanks, I know, I know... But really, credits go to the [Foundation HTML framework](https://foundation.zurb.com).

## Buy me a coffee

No thanks! I already had too much.

Paying your taxes is a healthier way to contribute to my salary.

## License

[Public domain](https://creativecommons.org/publicdomain/zero/1.0/), aka "do whatever you please with this code, it ain't mine".
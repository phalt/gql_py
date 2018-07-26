🌐🐍 gql.py
-------

_GraphQL Client for Pythonistas_

gql.py is a Pythonic interface around graphQL APIs.

You've probably got a graphQL API sitting on a webserver somewhere, and you want to talk to it, right?

GraphQL's use of HTTP is questionable at best, for those of us who love HTTP standards. But you can't deny graphQL's usefulness.

The goal of this library is to remove the fuss of HTTP so you can deal with graphQL directly. Just how graphQL's developers intended.

[![PyPi][pypi-image]][pypi-link]
[![CircleCI][circle-image]][circle-link]
[![Coverage Status][codecov-image]][codecov-link]
[![Landscape Status][landscape-image]][landscape-link]

```python

from gql_py import gql

query = '''
query ($bookId: ID!) {
    book(id: $bookId) {
      id
      title
      author
    }
  }
'''
variables = {
  'book_id': '654'
}

response = qgl.send(query=query, variables=variables)

response.ok
>>> True

response.errors
>>> None

response.data
>>> {'book': {'id': '654', 'title': 'Ursula K. Le Guin', 'title': 'A Wizard of Earthsea'}}

```

📖 Features
--------

- No need to handle the HTTP layer. (You can still set HTTP headers, though!)
- Responses come back as named tuples - even errors!
- Python 3.6+

✨ Future goals
---------------

- Draw graphQL queries & mutations with Python code.
- Hydrate API responses into Python objects.

🏗 Status
----------

gql.py is currently under development.


🎥 Credits
---------

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter).

We use [Python Requests](http://docs.python-requests.org/en/master/) for talking HTTP.


[pypi-image]: https://img.shields.io/pypi/v/gql_py.svg
[pypi-link]: https://pypi.python.org/pypi/gql_py
[pypi-dl-image]: https://img.shields.io/pypi/dm/gql_py.png
[circle-image]: https://circleci.com/gh/phalt/gql_py/tree/master.svg?style=svg
[circle-link]: https://circleci.com/gh/phalt/gql_py/tree/master
[codecov-image]: https://codecov.io/gh/phalt/gql_py/branch/master/graph/badge.svg?token=T9mYPv0Ep2
[codecov-link]: http://codecov.io/github/phalt/gql_py?branch=master
[landscape-image]: https://landscape.io/github/phalt/gql_py/master/landscape.svg?style=flat&badge_auth_token=0cce4803ec014cf4ad889498bba7e7e7
[landscape-link]: https://landscape.io/github/phalt/gql_py/master

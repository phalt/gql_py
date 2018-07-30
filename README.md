🌐🐍 gql.py
-------

_GraphQL Client for Pythonistas_

gql.py is a Pythonic interface around graphQL APIs.

You've got a graphQL API, and you want to talk to it, right? For those of us who love HTTP standards, GraphQL's use of HTTP is questionable at best. The goal of this library is to remove the fuss of HTTP so you can deal with graphQL directly. Just how graphQL's developers intended.

[![PyPi][pypi-image]][pypi-link]
[![PyPiV][pypi-image-v]][pypi-link]
[![PyPiL][pypi-image-l]][pypi-link]
[![PyPiS][pypi-image-s]][pypi-link]
[![CircleCI][circle-image]][circle-link]

```python

from gql_py import Gql

gql = Gql(api='https://example.com/graphql')

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
[pypi-image-v]: https://img.shields.io/pypi/pyversions/gql_py.svg
[pypi-image-l]: https://img.shields.io/pypi/l/gql_py.svg
[pypi-image-s]: https://img.shields.io/pypi/status/gql_py.svg
[pypi-link]: https://pypi.org/project/gql-py/
[pypi-dl-image]: https://img.shields.io/pypi/dm/gql_py.png
[circle-image]: https://circleci.com/gh/phalt/gql_py/tree/master.svg?style=svg
[circle-link]: https://circleci.com/gh/phalt/gql_py/tree/master

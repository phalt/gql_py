🌐🐍 gql_py
-------

*GraphQL Client for Pythonistas*

gql_py is a Pythonic interface around graphQL APIs.

You've got a graphQL API, and you want to talk to it, right? For those of us who love HTTP standards, GraphQL's use of HTTP is questionable at best. The goal of this library is to remove the fuss of HTTP so you can deal with graphQL directly. Just how graphQL's developers intended.


.. image:: https://img.shields.io/pypi/v/gql_py.svg
        :target: https://pypi.org/project/gql-py/

.. image:: https://img.shields.io/pypi/pyversions/gql_py.svg
        :target: https://pypi.org/project/gql-py/

.. image:: https://img.shields.io/pypi/l/gql_py.svg
        :target: https://pypi.org/project/gql-py/

.. image:: https://img.shields.io/pypi/status/gql_py.svg
        :target: https://pypi.org/project/gql-py/

.. image:: https://circleci.com/gh/phalt/gql_py/tree/master.svg?style=svg
        :target: https://circleci.com/gh/phalt/gql_py/tree/master

Installing the project is easy:

.. code-block:: bash

    pip install gql_py

Full blown example:

.. code-block:: python

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


You can validate your graphql query string by passing the __validate__ flag in the __send__ method:

.. code-block:: python

    gpl.send(query=query, validate=True)
    >>> Traceback (most recent call last):
    >>>     graphql.error.syntax_error.GraphQLSyntaxError: Syntax Error: Expected Name, found }


📖 Features
--------

- No need to handle the HTTP layer. (You can still set HTTP headers, though!)
- Responses come back as named tuples - even errors!
- Validate your query strings easily.
- Python 3.6+

✨ Future goals
---------------

- Hydrate API responses into custom Python objects.

🏗 Status
----------

gql.py is currently under development.

🎥 Credits
-----------

This package was created with Cookiecutter_.

We use `Python Requests`_ for talking HTTP.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`Python Requests`: https://github.com/audreyr/cookiecutter-pypackage

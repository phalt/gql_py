#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `gql_py` package."""

import pytest

from gql_py import Gql


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_object(response):
    gql = Gql(api='http://test.com')
    assert gql.api == 'http://test.com'

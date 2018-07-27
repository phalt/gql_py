# -*- coding: utf-8 -*-

"""Main module."""

import re
from typing import Mapping, Any, Optional

EXTRA_WHITE_SPACE = re.compile(r'\s{2,}')


def normalise_query(query: str) -> str:
    """
    Strip redundant white space from the query string to save space.
    """
    return EXTRA_WHITE_SPACE.sub(' ', query.strip())


def camelcase_variables(variables: Mapping[str, Any]) -> Mapping[str, Any]:
    """
    Transform typical python underscore-style variables
    into camelCased variables that graphQL expects.
    NOTE: Converts nested dictionaries recursively so all keys are camelCased.
    """
    def convert(string):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    for key, value in


def send(
    *,
    query: str,
    variables: Mapping[str, Any] = None,
    heades: Mapping[str, Any] = None,
) -> 'GraphQLResponse':

    cleaned_query = normalise_query(query)
    camelcase_variables = camelcase_variables(variables)

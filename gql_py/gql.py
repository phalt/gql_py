# -*- coding: utf-8 -*-

"""Main module."""

import re
from collections import namedtuple
from typing import Any, Mapping, Optional

import requests

EXTRA_WHITE_SPACE = re.compile(r'\s{2,}')


def normalise_query(query: str) -> str:
    """
    Strip redundant white space from the query string to save space.
    """
    return EXTRA_WHITE_SPACE.sub(' ', query.strip())


def to_camelcase(variables: Mapping[str, Any]) -> Mapping[str, Any]:
    """
    Transform typical python underscore-style variables
    into camelCased variables that graphQL expects.
    NOTE: Converts nested dictionaries recursively so all keys are camelCased.
    """
    def convert(string):
        # thanks to https://stackoverflow.com/a/1176023/1327062
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    converted_dict = {}
    for key, value in variables.items():
        if isinstance(value, dict):
            value = to_camelcase(value)
        key = convert(key)
        converted_dict[key] = value
    return converted_dict


def prepared_payload(
    *,
    cleaned_query: str,
    camelcased_variables: Optional[Mapping[str, Any]],
) -> Mapping[str, Any]:
    return {
        'query': cleaned_query,
        'variables': camelcased_variables,
    }


GraphQLResponse = namedtuple(
    'GraphQLResponse', ('errors', 'ok', 'data'),
)


class Gql:
    """
    Base class for graphQL HTTP queries
    """
    def __init__(
        self, *,
        api: str,
        session: Optional['requests.Session'] = None,
        default_headers: Optional[Mapping[str, Any]] = None,
    ) -> None:
        self.api = api
        self.session = session or requests.Session()
        if default_headers:
            self.session.headers.update(default_headers)

    def generate_result(
        self, result: 'requests.Response'

    ) -> 'GraphQLResponse':
        json_data = result.json()
        return GraphQLResponse(
            errors=json_data.get('errors') or None,
            ok=result.status_code == 200 and not json_data.get('errors', []),
            data=json_data.get('data'),
        )

    def send(
        self, *,
        query: str,
        variables: Optional[Mapping[str, Any]] = None,
        headers: Mapping[str, Any] = None,
    ) -> 'GraphQLResponse':

        cleaned_query = normalise_query(query)
        camelcased_variables = to_camelcase(variables) if variables else None
        payload = prepared_payload(
            cleaned_query=cleaned_query,
            camelcased_variables=camelcased_variables,
        )
        all_headers = self.session.headers
        if headers:
            all_headers.update(**headers)
        req = requests.Request(
            url=self.api, method='POST', json=payload, headers=headers
        )
        prepared_request = self.session.prepare_request(req)
        result = self.session.send(prepared_request)
        return self.generate_result(result)

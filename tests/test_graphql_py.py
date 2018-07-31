#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `gql_py` package."""

import json

import pytest
import responses

from gql_py import Gql, normalise_query, to_camelcase


def test_basic_object():
    gql = Gql(api='http://test.com')
    assert gql.api == 'http://test.com'


@responses.activate
def test_headers_are_set():
    responses.add(responses.POST, 'http://test.com/graphql',
                  body='''
                    {"errors": [], "data": {"title": "blog title"}}''',
                  status=200,
                  content_type='application/json')
    gql = Gql(api='http://test.com/graphql')
    gql.send(query='query \{\}', variables={}, headers={'foo': 'bar'})
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://test.com/graphql'
    assert 'foo' in responses.calls[0].request.headers.keys()


@responses.activate
def test_headers_are_set_during_object_creation():
    responses.add(responses.POST, 'http://test.com/graphql',
                  body='''
                    {"errors": [], "data": {"title": "blog title"}}''',
                  status=200,
                  content_type='application/json')
    gql = Gql(api='http://test.com/graphql', default_headers={'foo': 'bar'})
    gql.send(query='query {}', variables={})
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://test.com/graphql'
    assert 'foo' in responses.calls[0].request.headers.keys()


@responses.activate
def test_good_formatted_data_is_sent():
    responses.add(responses.POST, 'http://test.com/graphql',
                  body='''
                    {"errors": [], "data": {"title": "blog title"}}''',
                  status=200,
                  content_type='application/json')
    gql = Gql(api='http://test.com/graphql')
    query = '''
        query ($someValue: ID){
            concept(id: $someValue){
                name
            }
        }

    '''
    gql.send(
        query=query,
        variables={'some_value': 'bar'},
        headers={'foo': 'bar'}
    )
    http_call = responses.calls[0].request
    json_post_data = json.loads(http_call.body)
    assert json_post_data['variables'] == {'someValue': 'bar'}
    assert json_post_data['query'] == (
        'query ($someValue: ID){ concept(id: $someValue){ name } }'
    )


@responses.activate
def test_good_response():
    responses.add(responses.POST, 'http://test.com/graphql',
                  body='''
                    {"errors": [], "data": {"title": "blog title"}}''',
                  status=200,
                  content_type='application/json')
    gql = Gql(api='http://test.com/graphql')
    result = gql.send(query='query \{\}', variables={}, headers={'foo': 'bar'})
    assert result.errors is None
    assert result.ok
    assert result.data == {'title': 'blog title'}


@responses.activate
def test_bad_response():
    responses.add(responses.POST, 'http://test.com/graphql',
                  body='''
                    {"errors": [{"message": "some error"}], "data": {}}''',
                  status=200,
                  content_type='application/json')
    gql = Gql(api='http://test.com/graphql')
    result = gql.send(query='query \{\}', variables={}, headers={'foo': 'bar'})
    assert result.errors == [{'message': 'some error'}]
    assert not result.ok
    assert result.data is None


@pytest.mark.parametrize('input, output', [
    (
        {'some_variable': 'value'}, {'someVariable': 'value'}
    ),
    (
        {'nested': {'change_me': 'value'}}, {'nested': {'changeMe': 'value'}}
    ),
    (
        {'ignoreMe': 'value'}, {'ignoreMe': 'value'}
    )
])
def test_to_camel_case(input, output):
    assert to_camelcase(input) == output


def test_normalise_query():
    query = '''
        query ($someValue: ID){
            concept(id: $someValue){
                name
            }
        }

    '''
    assert normalise_query(query) == (
        'query ($someValue: ID){ concept(id: $someValue){ name } }'
    )

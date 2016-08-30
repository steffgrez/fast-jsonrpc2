import pprint

import json
import pytest

from fast_jsonrpc2 import JSONRPCResolver


def subtract(minuend, subtrahend):
    return minuend - subtrahend


def raise_error():
    raise Exception('error')


def update(a, b, c, d, e):
    pass


def foobar(msg):
    return 'foobar ' + str(msg)


def notify():
    pass

router = {
    'subtract': subtract,
    'update': update,
    'foobar': foobar,
    'raise_error': raise_error,
    'notify': notify,
}

resolver = JSONRPCResolver(router, error_verbose=False)


@pytest.mark.parametrize('query,expected', [
    # (
    #     """{"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": 1}""",  # NOQA
    #     """{"jsonrpc": "2.0", "result": 19, "id": 1}"""
    # ),
    # (
    #     """{"jsonrpc": "2.0", "method": "foobar", "params": ["toto"], "id": 1}""",  # NOQA
    #     """{"jsonrpc": "2.0", "result": "foobar toto", "id": 1}"""
    # ),
    # (
    #     """{"jsonrpc": "2.0", "method": "subtract", "params": [23, 42], "id": 2}""",  # NOQA
    #     """{"jsonrpc": "2.0", "result": -19, "id": 2}"""
    # ),
    # (
    #     """{"jsonrpc": "2.0", "method": "subtract", "params": {"subtrahend": 23, "minuend": 42}, "id": 3}""",  # NOQA
    #     """{"jsonrpc": "2.0", "result": 19, "id": 3}"""
    # ),
    # (
    #     """{"jsonrpc": "2.0", "method": "subtract", "params": {"minuend": 42, "subtrahend": 23}, "id": 4}""",  # NOQA
    #     """{"jsonrpc": "2.0", "result": 19, "id": 4}"""
    # ),
    # (
    #     """{"jsonrpc": "2.0", "method": "update", "params": [1, 2, 3, 4, 5]}""",  # NOQA
    #     ''
    # ),
    # (
    #     """{"jsonrpc": "2.0", "method": "notify"}""",
    #     ''
    # ),
    # (
    #     """{"jsonrpc": "2.0", "method": "foobar2", "id": "1"}""",
    #     """{"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": "1"}"""  # NOQA
    # ),
    # (
    #     """{"jsonrpc": "2.0", "method": "foobar, "params": "bar", "baz"]""",
    #     """{"jsonrpc": "2.0", "error": {"code": -32700, "message": "Parse error"}, "id": null}"""  # NOQA
    # ),
    (
        """{"jsonrpc": "2.0", "method": 1, "params": "bar"}""",
        """{"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid Request"}, "id": null}"""  # NOQA
    ),
    # (
    #     """{"jsonrpc": "2.0", "method": "subtract", "params": [23], "id": 1}""",  # NOQA
    #     """{"jsonrpc": "2.0", "error": {"code": -32602, "message": "Invalid params"}, "id": 1}"""  # NOQA
    # ),
    # (
    #     """{"jsonrpc": "2.0", "method": "raise_error", "id": 1}""",  # NOQA
    #     """{"jsonrpc": "2.0", "error": {"code": -32603, "message": "Internal error"}, "id": 1}"""  # NOQA
    # ),
    # (
    #     """{"jsonrpc": "2.0", "method": "foobar", "params": "toto", "id": 1}""",  # NOQA
    #     """{"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid Request"}, "id": 1}"""  # NOQA
    # ),
])
def test_init(query, expected):
    decoded_expected = json.loads(expected) if expected else expected
    result = resolver.handle(query)
    decoded_result = json.loads(result) if result else result

    pprint.pprint(decoded_expected)
    pprint.pprint(decoded_result)
    assert decoded_expected == decoded_result

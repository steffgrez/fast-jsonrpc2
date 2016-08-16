
import json
import pytest

from fast_jsonrpc2 import JSONRPCResolver


def subtract(minuend, subtrahend):
    return minuend - subtrahend


def sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total


def notify_sum(a, b, c):
    pass


def notify_hello(hello):
    pass


def update(a, b, c, d, e):
    pass


def foobar():
    pass


def get_data():
    return ["hello", 5]

router = {
    'subtract': subtract,
    'sum': sum,
    'notify_hello': notify_hello,
    'update': update,
    'foobar': foobar,
    'get_data': get_data,
    'notify_sum': notify_sum,
}

resolver = JSONRPCResolver(router, error_verbose=False)


@pytest.mark.parametrize('query,expected', [
    (
        """
        [
            {"jsonrpc": "2.0", "method": "sum", "params": [1,2,4], "id": "1"},
            {"jsonrpc": "2.0", "method"
        ]
        """,
        """
            {"jsonrpc": "2.0", "error": {"code": -32700, "message": "Parse error"}, "id": null}
        """  # NOQA
    ),
    (
        """[]""",
        """{"error": {"code": -32600, "message": "Invalid Request"}, "id": null, "jsonrpc": "2.0"}"""  # NOQA
    ),
    (
        """[1]""",
        """[{"error": {"code": -32600, "message": "Invalid Request"}, "id": null, "jsonrpc": "2.0"}]"""  # NOQA
    ),
    (
        """[1,2,3]""",
        """
        [
            {"error": {"code": -32600, "message": "Invalid Request"}, "id": null, "jsonrpc": "2.0"},
            {"error": {"code": -32600, "message": "Invalid Request"}, "id": null, "jsonrpc": "2.0"},
            {"error": {"code": -32600, "message": "Invalid Request"}, "id": null, "jsonrpc": "2.0"}
        ]
        """  # NOQA
    ),
    (
        """
        [
            {"jsonrpc": "2.0", "method": "sum", "params": [1,2,4], "id": "1"},
            {"jsonrpc": "2.0", "method": "notify_hello", "params": [7]},
            {"jsonrpc": "2.0", "method": "subtract", "params": [42,23], "id": "2"},
            {"foo": "boo"},
            {"jsonrpc": "2.0", "method": "foo.get", "params": {"name": "myself"}, "id": "5"},
            {"jsonrpc": "2.0", "method": "get_data", "id": "9"}
        ]
        """,  # NOQA
        """
        [
            {"jsonrpc": "2.0", "result": 7, "id": "1"},
            {"jsonrpc": "2.0", "result": 19, "id": "2"},
            {"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid Request"}, "id": null},
            {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": "5"},
            {"jsonrpc": "2.0", "result": ["hello", 5], "id": "9"}
        ]
        """,  # NOQA
    ),
    (
        """
        [
            {"jsonrpc": "2.0", "method": "notify_sum", "params": [1,2,4]},
            {"jsonrpc": "2.0", "method": "notify_hello", "params": [7]}
        ]
        """,
        ""
    ),

])
def test_init(query, expected):
    decoded_expected = json.loads(expected) if expected else expected
    result = resolver.handle(query)
    decoded_result = json.loads(result) if result else result

    assert decoded_expected == decoded_result

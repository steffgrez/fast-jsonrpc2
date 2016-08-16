import pytest

from fast_jsonrpc2.router import (Router, RouterException)


def foobar():
    pass

a = 2


def test_init():
    # test simple case
    router = Router()
    assert len(set(router)) == 0

    # test with dict
    routes = {'a': foobar}
    router = Router(routes)
    shared_items = set(router.items()) & set(routes.items())
    assert len(shared_items) == len(routes)

    # test with wrong dict
    routes = {'a': 1}
    with pytest.raises(RouterException):
        router = Router(routes)

    # test with another thing
    with pytest.raises(RouterException):
        router = Router('a')


def test_add_method():
    router = Router()

    # with good one
    router.add_method('a', foobar)

    # with wrong one
    with pytest.raises(RouterException):
        router.add_method('a', a)

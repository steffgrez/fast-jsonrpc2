"""
from fast_jsonrpc import JSONRPCRequester

resquester = JSONRPCRequester()

requester.substract(args1, args2)
json_request = requester.get_request()

or

batch_requester = requester.batch()
batch_requester.substract(args1, args2)
batch_requester.add(args1, args2)

-----

requester.query(method, params, id)
requester.notify(method, params, id)


json_request = batch_requester.get_request()

"""


class JSONRPCRequester(object):
    def __init__(self):
        pass

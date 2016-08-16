

class Router(dict):
    def __init__(self, routes=None):
        if routes:
            if isinstance(routes, dict):
                for name, method in routes.iteritems():
                    self.add_method(name, method)
            else:
                raise RouterException(
                    'optional arg for Router ini must be a dict or a tuple'
                )

    def add_method(self, name, method):
        if callable(method):
            self[name] = method
        else:
            raise RouterException('{0} is not callable'.format(method))


class RouterException(Exception):
    pass

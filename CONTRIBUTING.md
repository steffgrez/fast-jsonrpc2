### Test coverage

.. code:: bash

    $ py.test --cov=fast_jsonrpc2 --cov-report term-missing tests/


### Linter

.. code:: bash

    $ pylint fast_jsonrpc2


### Cyclomatic Complexity

.. code:: bash

    $ xenon --max-absolute B --max-modules A --max-average A fast_jsonrpc2
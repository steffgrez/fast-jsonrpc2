#!/usr/bin/env python
import imp
import os
from os import path

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
VERSION = imp.load_source(
    'version',
    path.join(here, 'fast_jsonrpc2', 'version.py')
)
VERSION = VERSION.__version__
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read()

setup(
    name="fast-jsonrpc2",
    version=VERSION,
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    tests_require=["pytest", "mock", "py-cov"],
    install_requires=['six==1.10.0'],

    # metadata for upload to PyPI
    author="Lahache Stephane",
    url="https://github.com/steffgrez/fast-jsonrpc2",
    description="fast JSON-RPC protocol implementation, without transport",
    long_description=README + '\n\n' + CHANGES,
    keywords='json rpc jsonrpc json-rpc',

    # Full list:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        'Intended Audience :: Developers',
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    license="MIT",
)

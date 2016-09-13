#!/usr/bin/env python
import os
import sys
from os import path

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class ToxTest(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        else:
            args = []
        errno = tox.cmdline(args=args)
        sys.exit(errno)


here = os.path.abspath(os.path.dirname(__file__))
with open('fast_jsonrpc2/version.py') as f:
    exec(f.read())

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read()

setup(
    name="fast-jsonrpc2",
    version=__version__,
    packages=find_packages(),
    tests_require=['tox'],
    cmdclass = {'test': ToxTest},
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

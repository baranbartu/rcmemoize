#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages
from rcmemoize import __version__

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

packages = find_packages()

setup(
    name='rcmemoize',
    version=__version__,
    description='Cache anything in the current request cycle in memory for preventing duplicate method callers.',
    long_description=README,
    url='https://github.com/baranbartu/rcmemoize',
    download_url='https://github.com/baranbartu/rcmemoize/tarball/%s' % (
        __version__,),
    author='Baran Bartu Demirci',
    author_email='bbartu.demirci@gmail.com',
    license='MIT',
    keywords='django,memoize,memorize,cache,cached,cached property',
    packages=packages
)

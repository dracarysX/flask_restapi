#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


class MyTest(TestCommand):
    def run_tests(self):
        tests = unittest.TestLoader().discover('tests', pattern='test_*.py')
        unittest.TextTestRunner(verbosity=1).run(tests)


setup(
    name='flask_restapi',
    version='0.2.0',
    license='MIT',
    description=u'A simple rest query framework by flask, peewee, rest_query',
    author='dracarysX',
    author_email='huiquanxiong@gmail.com',
    url='https://github.com/dracarysX/flask_restapi',
    packages=find_packages(include=['flask_restapi']),
    install_requires=[
        'peewee',
        'flask',
        'wtforms',
        'flask_bcrypt',
        'flask-script',
        'peewee-rest-query'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: MIT',
    ],
    keywords='Python, Flask, APIMethodView, Filtering Query API, Mysql, Peewee, RestAPI',
    long_description='A simple rest query framework. Web framework use flask, '
                     'orm by peewee, form by wtform and query by rest_query.'
                     'The framework implements custom query api(like this: /?select=id,name&id=gte.20), '
                     'save form data, model object serializer, APIMethodView(get， post， put，delete) and errorhandler.'
)

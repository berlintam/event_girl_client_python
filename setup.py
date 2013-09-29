#!/usr/bin/python2
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.txt') as file:
    long_description = file.read()

setup(
    name='eventgirl',
    version='0.1.dev1',
    packages=['eventgirl'],
    license='MIT',
    author="Tamara Eastley",
    author_email="tam.eastley@gmail.com",
    url="https://github.com/berlintam/event_girl_client_python",
    description="simple client for eventgirl",
    long_description=long_description,
)

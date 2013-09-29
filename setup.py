from setuptools import setup

with open('README.txt') as file:
    long_description = file.read()

setup(
    name='eventgirl',
    version='0.1.dev1',
    packages=['eventgirl'],
    license='MIT',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
)

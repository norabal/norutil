# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='norutil',
    version='0.0.1',
    description='Prototype package for my personal development',
    long_description=readme,
    author='Motoi Komatsu',
    author_email='norabal.works@gmail.com',
    url='https://github.com/norabal/norutil',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'nose',
        'sphinx'
    ]
)


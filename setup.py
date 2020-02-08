#!/usr/bin/env python
### cribbed from https://github.com/maet3608/minimal-setup-py/blob/master/setup.py
from setuptools import setup, find_packages

setup(
    name='check',
    version='0.5.2',
    url='https://github.com/SocialScienceWithOnlineData/check.git',
    author='Seth Frey',
    author_email='sfrey@ucdavis.edu',
    description='Interactive low-stakes local micro-assessments for notebook based Python pedagogy, originally for UC Davis course Social Science with Online Data',
    packages=find_packages(),
    license='MIT',
)

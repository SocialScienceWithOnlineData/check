#!/usr/bin/env python
### cribbed from https://github.com/maet3608/minimal-setup-py/blob/master/setup.py
from setuptools import setup, find_packages

setup(
    name='lessoncheck',
    version='0.5.2',
    url='https://github.com/enfascination/lessoncheck.git',
    author='Seth Frey',
    author_email='sfrey@ucdavis.edu',
    description='Interactive low-stakes local micro-assessments for notebook based Python pedagogy, for UC Davis CMN152V',
    packages=find_packages(),
    license='MIT',
)

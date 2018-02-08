#
# Initially copied from:
# https://raw.githubusercontent.com/pypa/sampleproject/master/setup.py
#

from setuptools import setup, find_packages
import os
import glob

quotes = glob.glob("quotes/*.txt")

setup(
    name='mulholland',

    version='0.0b1',

    description='Andrew Mulholland',
    long_description='Andrew Mulholland',

    author='Tim Golden',
    author_email='mail@timgolden.me.uk',

    license='MIT',

    packages=find_packages(),

    package_data={"mulholland" : ["quotes/*.txt"]}
)

#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

setup(
    name="edig",
    author="Carl Verstraete",
    description=("Extended dig program."),
    license="MIT",
    packages=find_packages(),
    scripts=['edig'],
    install_requires=['dnspython', 'geoip2', 'tld','ipwhois','mysql-connector-python'],
    python_requires='>3.4',
)

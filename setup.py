#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools


readme = '\n'.join(open('README.md').readlines())

setuptools.setup(
    name='dsr',
    version='1.0.2',

    # Project description
    description='Automatically gegerate repr to show data structures espelly trees',
    long_description=readme,
    long_description_content_type="text/markdown",

    # Author details
    author='Charles Xu',
    author_email='charl3s.xu@gmail.com',

    # Project details
    url='https://github.com/the0demiurge/DataStructureRepr',

    # Project dependencies
    classifiers=[
        "Programming Language :: Python",
        "License :: Other/Proprietary License",
        "Operating System :: Android",
        "Operating System :: iOS",
        "Operating System :: MacOS",
        "Operating System :: Microsoft",
        "Operating System :: Other OS",
        "Operating System :: POSIX",
        "Operating System :: Unix",
    ],
    packages=["dsr"],
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" setup.py for cookiecutter-bedrock."""

from setuptools import setup

__version__ = "0.1.0"

with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
    name="cookiecutter-bedrock",
    version=__version__,
    description="Cookiecutter template to create Bedrock projects.",
    long_description=long_description,
    author="Evandro Franco",
    url="https://github.com/evandrofranco/cookiecutter-bedrock",
    download_url="",
    packages=["boto3"],
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Framework :: Bedrock",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development",
    ],
    keywords=(
        """
        cookiecutter, Python, projects, project templates, bedrock,
        skeleton, aws, project directory, setup.py
        """
    ),
)
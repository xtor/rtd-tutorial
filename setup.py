#!/usr/bin/env python3

from setuptools import setup
import setuptools.command.build_py
from distutils.spawn import find_executable
import subprocess
from subprocess import check_call
import errno



setup(
        install_requires = ['protobuf >=3.21.12'],
)

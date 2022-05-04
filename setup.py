# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in posawesome/__init__.py
from IRDNepal import __version__ as version

setup(
	name='IRD Nepal',
	version=version,
	description='IRD Nepal',
	author='Param',
	author_email='vkparam@outlook.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
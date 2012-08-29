"""Installer for byebyepypi
"""

import os
cwd = os.path.dirname(__file__)
__version__ = open(os.path.join(cwd, 'src', 'byebyepypi', 'version.txt'), 'r').read().strip()

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    
setup(
    name='byebyepypi',
    description='Transparent pypi index cache',
    version=__version__,
    author='Tom Wardill',
    author_email='tom@howrandom.net',
    url='https://github.com/tomwardill/byebyepypi',
    packages=find_packages('src', exclude=['ez_setup']),
    install_requires=open(os.path.join(cwd, 'requirements.txt')).readlines(),
    package_dir={
        '': 'src',
        'byebyepypi': 'src/byebyepypi/'
    },
    package_data={'byebyepypi': ['version.txt']},
    include_package_data=True,
)

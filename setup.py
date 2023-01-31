#!/usr/bin/python3
# Setup script to install this package.
# M.Blakeney, Mar 2018.

from pathlib import Path
from setuptools import setup

name = 'edir'
module = name.replace('-', '_')
here = Path(__file__).resolve().parent

setup(
    name=name,
    version='2.16',
    description='Utility to rename, remove, and copy files/dirs using '
    'your editor',
    long_description=here.joinpath('README.md').read_text(),
    long_description_content_type='text/markdown',
    url=f'https://github.com/pi314/{name}',
    author='Chang-Yen Chih',
    author_email='michael66230@gmail.com',
    keywords='vidir',
    license='GPLv3',
    py_modules=[module],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    data_files=[
        (f'share/{name}', ['README.md']),
    ],
    entry_points={
        'console_scripts': [f'{name}={module}:main'],
    },
)

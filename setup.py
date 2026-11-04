#!/usr/bin/env python
import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='fellow-aiden',
    version='0.2.3',
    description='Interface for interacting with Fellow Aiden coffee brewer',
    url='https://github.com/9b/fellow-aiden',
    author="Brandon Dixon",
    author_email="brandon@9bplus.com",
    license="GNUV3",
    packages=find_packages(),
    install_requires=[
        'requests>=2.32.3',
        'pydantic>=2.10.4'
    ],
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
    package_data={
        'fellow_aiden': [],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=['coffee', 'coffee brewer', 'fellow', 'coffee tech'],
    extras_require={
        'dev': [
            'pytest>=6.2',
            'black>=21.9b0'
        ]
    }
)
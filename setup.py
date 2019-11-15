#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirements = [
    "numpy==1.17.2",
    "JPype1==0.7.0"
    ]


setup(
    name='python-heideltime',
    version='0.0.1',
    description="This is a python wrapper for the multilingual temporal tagger HeidelTime",
    long_description=readme,
    
    url='https://github.com/amineabdaoui/python-heideltime',
    packages=find_packages(include=['HeidelTime','TreeTagger']),
    entry_points={        
    },
    include_package_data=True,
    package_data={'': ['LICENSE','config.props'],
                  'HeidelTime':['de.unihd.dbs.heideltime.standalone.jar']},
    data_files=[('', ['LICENSE','config.props']),
                ('HeidelTime', ['de.unihd.dbs.heideltime.standalone.jar'])],
    install_requires=requirements,
    zip_safe=False,
    keywords='python-heideltime',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
    
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]    
)
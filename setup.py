#!/usr/bin/env python

import os
import setuptools

VERSION = '0.1.1'

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setuptools.setup(
    name='pyglib',
    author='Benjamin Staffin',
    author_email='benley@gmail.com',
    url='https://github.com/benley/pyglib',
    install_requires=[
        'python-gflags',
        'glog>=0.3',
    ],
    description='Opinionated but handy app startup wrapper.',
    long_description=README,
    packages=['pyglib'],
    license='BSD',
    version=VERSION,
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: System :: Logging',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms='any',
)

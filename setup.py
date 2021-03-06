#!/usr/bin/env python

# Support setuptools or distutils
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Import ourselves for version info
import patchwork

# Frankenstein long_description: version-specific changelog note + README
v = patchwork.__version__
long_description = """
To find out what's new in this version of Patchwork, please see `the changelog
<http://docs.patchwork.fabfile.org/en/%s/changelog.html>`_.

%s
""" % (v, open('README.rst').read())

setup(
    name='patchwork',
    version=v,
    description='Common deploy/sysadmin operations',
    license='BSD',

    long_description=long_description,
    author='Jeff Forcier',
    author_email='jeff@bitprophet.org',
    url='http://patchwork.fabfile.org',

    packages=["patchwork"],

    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Software Distribution',
          'Topic :: System :: Systems Administration',
    ],
)

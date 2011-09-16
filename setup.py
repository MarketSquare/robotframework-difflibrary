#!/usr/bin/env python

from distutils.core import setup

from os.path import abspath, dirname, join
execfile(join(dirname(abspath(__file__)), 'src', 'DiffLibrary', 'version.py'))

DESCRIPTION = """
Robot Framework keyword library that will provide keyword functionality to diff two fules together .
"""[1:-1]


CLASSIFIERS = """
Development Status :: 5 - Production/Stable
License :: Public Domain
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

setup(name         = 'robotframework-difflibrary',
      version      = VERSION,
      description  = 'Robot Framework keyword library for textual diffing',
      long_description = DESCRIPTION,
      author       = 'Bulkan Savun Evcimen',
      author_email = 'bulkan@gmail.com',
      url          = 'http://github.com/bulkan/robotframework-difflibrary',
      license      = 'Public Domain',
      keywords     = 'robotframework testing test automation diff textual',
      platforms    = 'any',
      classifiers  = CLASSIFIERS.splitlines(),
      package_dir  = {'' : 'src'},
      packages     = ['DiffLibrary'],
      #package_data = {'DiffLibrary': ['tests/*.txt']}
      )

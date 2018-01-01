#!/usr/bin/env python

'''
    setup
    _____

    This is the main setup script for Nem Core API.

    :copyright: (c) 2017-2018 QChain, Inc. All Rights Reserved.
    :license: Apache, see LICENSE for more details.
'''

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# SETTINGS
# --------


DEPENDENCIES = ['aiohttp']

SHORT_DESCRIPTION = 'Asynchronous wrapper for the NEM NIS REST API.'

#LONG_DESCRIPTION = '''Cross-Link Discoverer, or XL Discoverer aims
#to provide a complete toolkit accessible from a GUI for cross-linking
#mass spectrometry identification, validation, and quantitation.
#
#XL Discoverer also supports various file formats, including open source
#formats, such as mzML, mzXML, MGF, as well as proprietary file formats
#such as Thermo Raw Files.
#'''

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Operating System :: Unix',
    'Operating System :: POSIX :: Linux',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
]


# SETUP
# -----

setup(name='Nem NIS API',
      version='0.1.0',
      description=SHORT_DESCRIPTION,
#      long_description=LONG_DESCRIPTION,
      classifiers=CLASSIFIERS,
      author='QChain, Inc.',
      author_email='ahuszagh@qchain.co',
      maintainer='Alex Huszagh',
      maintainer_email='ahuszagh@qchain.co',
      packages=['nem_nis'],
      package_data={'': [
          'licenses/*',
          'resources/png/*',
          'templates/*',
          'README.md',
      ]},
      include_package_data=True,
      install_requires=DEPENDENCIES,
      setup_requires=DEPENDENCIES,
      zip_safe=True,
     )

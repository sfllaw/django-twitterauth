#!/usr/bin/env python

from distutils.core import setup

setup(name='django-twitterauth',
      version='0.1',
      description='Use Twitter for authentication in Django',
      author='Richard Crowley',
      author_email='r@rcrowley.org',
      url='http://rcrowley.org/2009/01/24/django-twitterauth',
      packages=['twitterauth'],
      package_dir={'twitterauth': '.'},
      package_data={'twitterauth': ['templates/*']},
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: Other/Proprietary License',
          'Operating System :: OS Independent',
          'Programming Language :: Python'],
      license='Creative Commons Attribution-Share Alike 3.0 Unported License')


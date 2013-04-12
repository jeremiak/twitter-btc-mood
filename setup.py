#!/usr/bin/env python

from distutils.core import setup

setup(name='Twitter BTC',
      version='0.1',
      description='Super rough (to the point of being almost the opposite of science) sentiment analysis of Bitcoins using the Twitter Streaming API',
      author='Jeremia Kimelman',
      author_email='jbkimelman@gmail.com    ',
      url='http://www.github.com/jeremiak/twitter-btc-mood',
      packages = ['script'],
      install_requires=['twitter', 'pattern']
     )

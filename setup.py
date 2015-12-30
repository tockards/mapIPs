#!/usr/bin/env python

from distutils.core import setup

setup(name='IPsToMap',
      version='1.0',
      description='Geolocates IPs and displays them on a MAP.',
      author='Toufeeq Ockards',
      author_email='toufeeq.ockards+github@gmail.com',
      url='https://github.com/tockards',
      install_requires=['geoip2', 'folium'],
      scripts=['scripts/map_ips'],
     )

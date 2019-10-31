"""
Author: exlab247@gmail.com
[dd/mm/yyyy]: 25/09/2019

sudo -u homeassistant -H -s
source /srv/homeassistant/bin/activate
python3 -m pip install pyserial
"""
def __bootstrap__(so_file):
   global __bootstrap__, __loader__, __file__
   import sys, pkg_resources, imp
   __file__ = pkg_resources.resource_filename(__name__, so_file)
   __loader__ = None; del __bootstrap__, __loader__
   imp.load_dynamic(__name__,__file__)
so_file = 'alarm_gateway.so'
__bootstrap__(so_file)

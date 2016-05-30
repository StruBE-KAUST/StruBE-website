# -*- coding : utf-8 -*-

##    Copyright (C) 2015 Hungler Arnaud
##
##    This program is free software; you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation; either version 2 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License along
##    with this program; if not, write to the Free Software Foundation, Inc.,
##    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import ConfigParser
import os
import errno

config = ConfigParser.ConfigParser()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = os.path.join(BASE_DIR, "config.ini")
config.read(config_file)

log_path_rel = config.get('PATHS', 'log')
log_path = os.path.join(BASE_DIR, log_path_rel)

LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'sysform': {
                'format': '%(asctime)s StruBE[%(process)s] <%(levelname)s> %(message)s'
                },
            'detailed': {
                'format': '%(asctime)s StruBE[%(process)s] (%(name)s.%(funcName)s:%(lineno)s) <%(levelname)s> %(message)s'
                },
            },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'sysform',
                'level': 'INFO'
                },
            'info_file': {
                'class' : 'logging.handlers.RotatingFileHandler',
                'filename': log_path + "info.log",
                'formatter': 'sysform',
                'level': 'INFO'
                },
            'debug_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': log_path + "debug.log",
                'formatter': 'detailed',
                'level': 'DEBUG'
                },
            },
        'loggers': {
            '': {
                'handlers': ['console', 'info_file', 'debug_file'],
                'level': 'DEBUG'
                },
            'django': {
                'handlers': ['info_file'],
                'level': 'INFO'
                },
            },
        }

# Create log files
try:
    os.makedirs(log_path)
except OSError as e:
    if e.errno == errno.EEXIST and os.path.isdir(log_path):
        pass
    else:
        raise

with open(LOGGING['handlers']['info_file']['filename'], 'w+'):
    pass
with open(LOGGING['handlers']['debug_file']['filename'], 'w+'):
    pass

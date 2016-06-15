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

LOGGING = {
        'version': 1,
        'disable_exisiting_loggers': False,
        'formatters': {
            'sysform': {
                'format': 'StruBE[%(process)s] (%(name)s:%(lineno)s) <%(levelname)s> %(message)s'
                },
            },
        'handlers': {
            'syslog6': {
                'class': 'logging.handlers.SysLogHandler',
                'level': 'INFO',
                'address': '/dev/log',
                'facility': 'local6',
                'formatter': 'sysform',
                },
            },
        'loggers': {
            '': {
                'handlers': ['syslog6'],
                'level': 'INFO',
                },
            'django': {
                'handlers': ['syslog6'],
                'level': 'INFO',
                },
            }
        }

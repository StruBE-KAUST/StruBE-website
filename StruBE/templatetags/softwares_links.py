# -*- coding : utf-8 -*-

##    Copyright (C) 2017 King Abdullah University of Science and Technology
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

from django import template
from django.urls import reverse
from django.apps import apps

register = template.Library()

@register.inclusion_tag('softwares_links.html')
def software_links():
    custom_apps = []
    if apps.is_installed('contaminer'):
        custom_apps.extend([
            {'name': 'ContaMiner', 'href': reverse('ContaMiner:home')},
            {'name': 'ContaBase', 'href': reverse('ContaMiner:contabase')},
            ])

    return {'links': custom_apps}

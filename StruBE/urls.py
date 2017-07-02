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

from django.conf.urls import include, url
from django.contrib import admin
from django.apps import apps
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$',
        TemplateView.as_view(template_name="home.html"),
        name='home'),
    url(r'^admin/',
        admin.site.urls),
    url(r'^account/',
        include('myaccount.urls')),
    url(r'^contact/',
        views.MyContactView.as_view(), name="envelope-contact"),
    url(r'^contact/',
        views.MyContactView.as_view(), name="contact"),
    url(r'^tinymce/',
        include('tinymce.urls')),
    url(r'^labdir/',
        TemplateView.as_view(template_name="labdir.html"),
        name='labdir'),
    url(r'^instruments/',
        TemplateView.as_view(template_name="instruments.html"),
        name='instruments'),
]

if apps.is_installed('contaminer'):
    urlpatterns.append(
        url(r'^contaminer/',
            include('contaminer.urls', namespace="ContaMiner")))

if apps.is_installed('ProteinViewer'):
    urlpatterns.append(
        url(r'^viewer/',
            include('ProteinViewer.urls', namespace="ProteinViewer")))

if apps.is_installed('NMRViewer'):
    urlpatterns.append(
        url(r'^nmrviewer/',
            include('NMRViewer.urls', namespace="NMRViewer")))

handler403 = 'StruBE.views.custom403'
handler404 = 'StruBE.views.custom404'
handler500 = 'StruBE.views.custom500'

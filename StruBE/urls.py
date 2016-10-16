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
from . import views
import news.views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('myaccount.urls')),
    url(r'^contact/', views.MyContactView.as_view(), name="envelope-contact"),
    url(r'^contact/', views.MyContactView.as_view(), name="contact"),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^people/', views.people, name="people"),
    url(r'^labdir/', views.labdir, name="labdir"),
    url(r'^instruments/', views.instruments, name="instruments"),
    url(r'^contaminer/', include('contaminer.urls', namespace="ContaMiner")),
    url(r'^publications/', include('publications.urls',
        namespace="Publications")),
    url(r'^news/', include('news.urls', namespace="news")),
]

handler403 = 'StruBE.views.custom403'
handler404 = 'StruBE.views.custom404'
handler500 = 'StruBE.views.custom500'

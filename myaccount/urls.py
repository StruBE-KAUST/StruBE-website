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

from .views import MyLoginView
from .views import MySignupView
from .views import MySettingsView

urlpatterns = [
        url(r'^login', MyLoginView.as_view(),
            name='account_login'),
        url(r'^signup', MySignupView.as_view(),
            name='account_signup'),
        url(r'^password_reset', MySignupView.as_view(),
            name='account_password_reset'),
        url(r'^settings', MySettingsView.as_view(),
            name='account_settings'),
        url(r'^', include("account.urls")),
]


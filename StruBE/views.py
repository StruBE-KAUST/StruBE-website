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

from django.shortcuts import render
from django.contrib import messages
from envelope.views import ContactView
from braces.views import FormMessagesMixin
from .forms import MyContactForm
import logging

def home(request):
    return render(request, 'home.html')

class MyContactView(FormMessagesMixin, ContactView):
    template_name = "envelope/contact.html"
#TODO : success_url = reverse(qqch)
    form_class = MyContactForm
    form_valid_message = "Thanks for your message !"
    form_invalid_message = "Something went wrong. Please be sure to fill in the form correctly"

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

from django.views.generic.base import TemplateView
from django.middleware.csrf import rotate_token

from account.views import LoginView
from account.views import SignupView
from .forms import MyLoginForm
from .forms import MySignupForm

class MyLoginView(LoginView):
    form_class = MyLoginForm

    def form_invalid(self, form):
        rotate_token(self.request)
        return super(MyLoginView, self).form_invalid(form)

    def form_valid(self, form):
        rotate_token(self.request)
        return super(MyLoginView, self).form_valid(form)

class MySignupView(SignupView):
    form_class = MySignupForm

    def form_invalid(self, form):
        rotate_token(self.request)
        return super(MySignupView, self).form_invalid(form)

    def form_valid(self, form):
        rotate_token(self.request)
        return super(MySignupView, self).form_valid(form)

    def generate_username(self, form):
        return form.cleaned_data['email']

class MySettingsView(TemplateView):
    template_name = "account/settings.html"


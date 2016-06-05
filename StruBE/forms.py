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

from envelope.forms import ContactForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class MyContactForm(ContactForm):
    def __init__(self, *args, **kwargs):
        super(MyContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit(
            'submit',
            'Submit',
            css_class='btn-primary'))

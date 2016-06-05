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


from django.shortcuts import render, redirect

from django.views.generic.edit import FormView

from . import models, forms
from django.views.generic import CreateView, RedirectView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout, login, authenticate
from django.views import View
from django.contrib.auth.views import LoginView as LogView

class SignupView(CreateView):
    template_name = 'users/signup.html'
    form_class = forms.UserSignupForm
    success_url = reverse_lazy('users:login')

class LoginView(LogView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('app1:indexpage')
    form_class = forms.UserLoginForm
    redirect_authenticated_user = True

    # def get(self, request):
    #     return render(request, self.template_name,  {'form':forms.UserLoginForm(), 'invalid_creds': True})


    # def post(self, request):
    #     form = forms.UserLoginForm(request, request.POST)
    #     if form.is_valid():
    #         user = authenticate(request, username = form.cleaned_data.get('username'), password = form.cleaned_data.get('password'))
    #         if not user:
    #             return render(request, self.template_name, {'form':forms.UserLoginForm(), 'invalid_creds': True})


    #     login(request, user())
    #     return redirect(reverse('app1:indexpage'))


class LogoutView(RedirectView):
    url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)



from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label ='Enter Username', max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label ='Enter Password', max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control'}))

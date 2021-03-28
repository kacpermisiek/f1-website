from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(label='Login')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Hasło')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Potwierdź hasło')




    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password1',
                  'password2',
                  ]


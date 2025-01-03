from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
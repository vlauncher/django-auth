from django import forms
from users.models import User
from allauth.account.forms import SignupForm

class SignupForm(SignupForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
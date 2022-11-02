from allauth.account.views import SignupView,LoginView,LogoutView
from django.contrib.messages.views import SuccessMessageMixin

class SignUp(SignupView,SuccessMessageMixin):
    template_name = 'users/signup.html'
    success_message = 'Signup Success'

    


class Login(LoginView,SuccessMessageMixin):
    template_name = 'users/login.html'
    success_message = 'Login Successfull'


class Logout(LogoutView,SuccessMessageMixin):
    template_name = 'users/logout.html'
    success_message = 'Logged Out'


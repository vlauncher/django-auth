from django.urls import path
from users.views import SignUp,Logout,Login

urlpatterns = [
    path('signup/',SignUp.as_view(),name='account_signup'),
    path('login/',Login.as_view(),name='account_login'),
    path('logout/',Logout.as_view(),name='account_logout'),
]
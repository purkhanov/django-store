from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (EmailVerificationView, UserLoginView, UserProfileView,
                         UserRegistretionView)

app_name = 'users'

urlpatterns = [
    path('login', UserLoginView.as_view(), name = 'login'),
    path('registration', UserRegistretionView.as_view(), name = 'registration'),
    path('profile/<int:pk>', login_required(UserProfileView.as_view()), name = 'profile'),
    path('verify/<str:email>/<uuid:code>', EmailVerificationView.as_view(), name = 'email_verification'),
    path('logout', LogoutView.as_view(), name = 'logout'),
]

from django.urls import path
from django.contrib.auth.decorators import login_required
from users.views import UserLoginView, UserRegistretionView, UserProfileView
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('login', UserLoginView.as_view(), name = 'login'),
    path('registration', UserRegistretionView.as_view(), name = 'registration'),
    path('profile/<int:pk>', login_required(UserProfileView.as_view()), name = 'profile'),
    path('logout', LogoutView.as_view(), name = 'logout'),
]

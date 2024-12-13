from django.urls import path
from users.views import login, UserRegistretionView, profile, logout


app_name = 'users'

urlpatterns = [
    path('login', login, name = 'login'),
    path('registration', UserRegistretionView.as_view(), name = 'registration'),
    path('profile', profile, name = 'profile'),
    path('logout', logout, name = 'logout'),
]

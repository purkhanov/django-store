from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect, render
# from django.contrib.auth.decorators import login_required
# from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from products.models import Basket
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import EmailVerification, User


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Login'

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data = request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)

#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()

#     context = {'form': form}
#     return render(request, 'users/login.html', context)



class UserRegistretionView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Поздравляем! Вы успешно зарегистрировалиь!'
    title = 'Store - Регистрация'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Store - Регистрация'
    #     return context

# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data = request.POST)
#         if form.is_valid():
#             print("porm is valid")
#             form.save()
#             messages.success(request, 'Поздравляем! Вы успешно зарегистрировалиь!')
#             return HttpResponseRedirect(reverse("users:login"))
#     else:
#         form = UserRegistrationForm()

#     context = {'form': form }
#     return render(request, 'users/registration.html', context)


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store - Профиль'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = UserProfileForm(instance=request.user)
        
#     baskets = Basket.objects.filter(user=request.user)

#     context = {
#         'title': 'Store - Профиль',
#         'form': form,
#         'baskets': baskets,
#     }
#     return render(request, 'users/profile.html', context)


# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Store - Подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)

        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))

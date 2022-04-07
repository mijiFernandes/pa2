from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import AccessMixin
# from django.contrib.auth.models import User
from account.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from mysite import settings


class HomeView(TemplateView):
    template_name = 'home.html'


# Create your views here.
# 회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            )
            return redirect(to='register_done')
        return render(request, 'registration/register.html')
    else:
        form = UserCreationForm
        return render(request, 'registration/register.html', {'form': form})


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class LoginDoneTV(TemplateView):
    template_name = 'registration/login_done.html'


# 로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            try:
                points = settings.POINTS_SETTINGS['CREATE_ARTICLE']
            except KeyError:
                points = 0
            request.user.modify_points(points)
            return redirect(to='login_done')
        else:
            return render(request, 'registration/login.html', {'error': 'username or password is incorrect.'})
    else:
        form = AuthenticationForm
        return render(request, 'registration/login.html', {'form': form})


# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('home')


# home
def home(request):
    return render(request, 'home.html')


class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
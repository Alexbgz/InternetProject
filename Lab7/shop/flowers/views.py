from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Catalog, LoginForm, RegisterForm
from django.shortcuts import render,redirect, render_to_response
from django.http import HttpResponseRedirect
from django.views import View
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    params = {
        'phrase': 'Самый лучший магазин цветов'
    }
    return render(request, 'home.html', context=params)

def catalog(request):
    data = Catalog.objects.all()
    return render(request, 'catalog.html', {'catalog': data})

def product(request, id):
    data = Catalog.objects.filter(id=id)
    return render(request, 'product.html',  {'catalog': data})

class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'errors': '', 'form': form.as_p()})

    def post(self, request):
        form = RegisterForm(request.POST)

        if not form.is_valid():
            return render(request, 'register.html', {'errors': '', 'form': form.as_p()})

        u = User(username=form.cleaned_data['login'], email=form.cleaned_data['email'],
                 last_name=form.cleaned_data['lastname'], first_name=form.cleaned_data['firstname'])
        u.set_password(form.cleaned_data['password'])
        u.save()
        return redirect('/order')

class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form.as_p()})

    def post(self, request):
        log = request.POST['login']
        password = request.POST['password']
        errors = []

        user = authenticate(username=log, password=password)

        if user is not None:
            login(request, user)
            return redirect('/order')
        errors.append('Логин или пароль неверны')
        return render(request, 'login.html', {'errors': mark_safe('<br>'.join(errors)), 'login': login})

@login_required(login_url='/login')
def authOrder(request):
    a = 'Ваши заказы'
    return render(request, 'authOrder.html', {'auth': a})

class Logout(View):
    success_url = '/'
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
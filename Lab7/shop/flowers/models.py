from django.db import models
from django import forms
from django.contrib.auth.models import User

class Catalog(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    product = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    foto = models.CharField(max_length=255)

   # class Meta:
    #    db_table = 'catalog'

class LoginForm(forms.Form):
    login = forms.CharField(label='Логин', min_length=5)
    password = forms.CharField(label='Пароль', min_length=8, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    login = forms.CharField(label='Логин', min_length=5)
    password = forms.CharField(label='Пароль', min_length=8, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', min_length=8, widget=forms.PasswordInput)
    email = forms.CharField(label='Email', min_length=1)
    firstname = forms.CharField(label='Имя', min_length=1)
    lastname = forms.CharField(label='Фамлия', min_length=1)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Пароли не совпадают")
        usrs = User.objects.filter(username=cleaned_data.get('login'))
        if len(usrs) > 0:
            raise forms.ValidationError("Пользователь с данным логином уже существует")
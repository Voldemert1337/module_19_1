from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    age = forms.CharField(max_length=3, label='Введите свой возраст')
    password = forms.CharField(max_length=8, label='Введите пароль')
    repeat_password = forms.CharField(max_length=8, label='Повторите пароль')

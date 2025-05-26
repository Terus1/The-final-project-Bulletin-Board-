from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives
from django.core.mail import mail_admins


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30,
        label='Имя',
        widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'})
    )

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        subject = 'Добро пожаловать на нашу доску объявлений!'
        text = f'{user.first_name}, вы успешно зарегистрировались на сайте!'
        html = (
            f'<b>{user.first_name}</b>, вы успешно зарегистрировались на '
            f'<a href="http://127.0.0.1:8000/">сайте</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        mail_admins(
            subject='Зарегистрировался новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте'
        )
        return user

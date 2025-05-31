from django.dispatch import receiver
from allauth.account.signals import email_confirmed
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@receiver(email_confirmed)
def send_welcome_email(request, email_address, **kwargs):
    user = email_address.user

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


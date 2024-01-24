from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, send_mail
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.loader import get_template

from .models import Post, Reply


@receiver(post_save, sender=Reply)
def send_notification_about_reply(instance, created, **kwargs):
    '''Когда автор объявления получил отклик, то на его почту приходит уведомление.'''
    if created:
        mail = instance.post.author.email
        subject = 'Новый отклик на ваше объявление'
        text = f'Ваше объявление: {instance.post.title}\n' \
               f'Откликнулся: {instance.author}\n' \
               f'Текст отклика: {instance.text}'

        html = (f'<p>Ваше объявление: <b>{instance.post.title}</b></p>'
                f'<p>Откликнулся: <b>{instance.author}</b></p>'
                f'<p>Текст отклика: <b>{instance.text}</b></p>')

        # send_mail(subject,
        #           message,
        #           settings.DEFAULT_FROM_EMAIL,
        #           [mail])
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[mail]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()
        instance.save(update_fields=['status'])


@receiver(post_save, sender=Reply)
def send_email_notification(instance, **kwargs):
    ''' Когда автор принял отклик на своё объявление, то владельцу отклика на почту приходит уведомление. '''
    if instance.status is True:
        mail = instance.author.email
        subject = 'Ваш отклик был принят'
        text = f'Ваш отклик: "{instance.text}"\n' \
               f'На объявление: "{instance.post}"\n' \
               f'Был принят✔'

        html = (f'<p>Ваш отклик: <b>{instance.text}</b></p>'
                f'<p>На объявление: <b>{instance.post}</b><p>'
                f'<p>Был принят✔</p>')

        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[mail]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()
        # mail = instance.post.author.email
        # send_mail(
        #     'Уведомление',
        #     'На "Доске Объявлений" появилось новое объявление',
        #     settings.DEFAULT_FROM_EMAIL,
        #     [mail]
        # )

# @receiver(post_save, sender=User)
# def create_my_model(sender, instance, created, **kwargs):
#     if created:
#         Author.objects.create(user=instance, email=instance.email)


# @receiver(post_save, sender=Reply)
# def send_email_notification(instance, created, *args, **kwargs):
#     if created:
#         reaction = Reply.objects.get(id=instance.id)  # отклик в str представлении
#         reaction_text = reaction.text
#         post = Post.objects.get(pk=reaction.post_id)  # title поста
#         user = post.author
#         reaction_author = User.objects.get(pk=instance.user_id)  # тот чей отклик
#
#         subject = 'Пришёл отклик на ваше объявление'
#         from_email = 'coolloginpolzovatel@yandex.ru'
#         to_email = user.email
#         body_data = {
#             'reaction_author': reaction_author,
#             'reaction_text': reaction_text,
#             'post': post,
#             'reaction': reaction,
#             'user': user,
#         }
#         template = get_template('notification_email.html')
#         context = {
#             **body_data,
#         }
#         html_content = template.render(context)
#         send_mail(subject, html_content, from_email, [to_email])

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Автор поста')
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Описание')
    banner = models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка')
    time_in = models.DateTimeField(auto_now_add=True)  # атоматически добавляемая дата и время создания

    STATUS_CHOICES = (
        ('done', 'Выполнено'),
        ('no_done', 'Не выполнено'),
    )
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='no_done', verbose_name='Статус')

    CATEGORY_CHOICES = (
        ('tanks', 'Танки'),
        ('healing', 'Хилы'),
        ('merchants', 'Торговцы'),
        ('guildmasters', 'Гилдмастеры'),
        ('questgivers', 'Квестгиверы'),
        ('blacksmiths', 'Кузнецы'),
        ('tanners', 'Кожевники'),
        ('potionmakers', 'Зельевары'),
        ('spellmasters', 'Местера заклинаний')
    )
    category = models.CharField(max_length=12, choices=CATEGORY_CHOICES, default='tanks', verbose_name='Категория')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Автор отклика')
    text = models.CharField(max_length=256, verbose_name='Текст')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author} откликнулся на объявление: {self.post}'

    class Meta:
        verbose_name_plural = 'Отклики'
        verbose_name = 'Отклик'

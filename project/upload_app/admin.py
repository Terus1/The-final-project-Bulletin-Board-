from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

    # def save_model(self, request, obj, form, change):
    #     """
    #     Переопределяем метод сохранения модели
    #     """
    #     if not change:  # Проверяем что запись только создаётся
    #         obj.author = request.user  # Присваеваем полю автор текущего пользователя
    #
    #     super(PostAdmin, self).save_model(
    #         request=request,
    #         obj=obj,
    #         form=form,
    #         change=change
    #     )

admin.site.register(Post, PostAdmin)
admin.site.register(Reply)


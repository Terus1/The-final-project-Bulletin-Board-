from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['banner', 'title', 'text', 'category']

        widgets = {
            'text': SummernoteWidget(),
            'banner': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Напишите ваш отклик здесь...'
            }),
        }


class AcceptReplyForm(forms.ModelForm):
    choice = forms.ChoiceField(
        label='Решение по отклику',
        choices=[('accept', 'Принять'), ('reject', 'Отклонить')],
        widget=forms.RadioSelect,
        required=True
    )

    class Meta:
        model = Reply
        fields = []

    def save(self, commit=True):
        reply = super().save(commit=False)
        if self.cleaned_data['choice'] == 'accept':
            reply.status = True
        else:
            reply.status = False
        if commit:
            reply.save()
        return reply

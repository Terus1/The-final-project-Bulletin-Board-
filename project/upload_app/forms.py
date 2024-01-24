from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'category']

        widgets = {'text': SummernoteWidget()}


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['author', 'text']


class AcceptReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['status']

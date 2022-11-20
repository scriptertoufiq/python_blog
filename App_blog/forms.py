from django import forms
from App_blog.models import Blog,Comment
from django.forms import ModelForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

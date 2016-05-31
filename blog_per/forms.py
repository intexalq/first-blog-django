from django import forms
from .models import Post

from django.forms import widgets

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

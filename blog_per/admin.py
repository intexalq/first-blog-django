from django.contrib import admin
from .models import Post
from django import forms
from ckeditor.widgets import CKEditorWidget

admin.site.register(Post)

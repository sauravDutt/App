from dataclasses import fields
from unittest import mock
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
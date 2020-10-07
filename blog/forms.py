# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=250)
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = 'title', 'content', 'category', 'image', 'status',

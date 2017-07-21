from django import forms
from .models import Post, Comment


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'tag', 'content', 'post_status']


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'email', 'content']

from django import forms
from .models import Post, Comment


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'tag', 'content', 'post_status']

        widgets = {
            'content': forms.Textarea(attrs={'cols': 70, 'rows': 15})
        }


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'email', 'content']

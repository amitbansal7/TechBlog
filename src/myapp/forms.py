from django import forms
from .models import Post, Comment
from django.contrib.auth import get_user_model
from django.db.models import Q


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


class UserLoginForm(forms.Form):
    query = forms.CharField(label='username/email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        query = self.cleaned_data.get("query")
        password = self.cleaned_data.get("password")

        UserModel = get_user_model()
        user_qs = UserModel.objects.filter(
            Q(username__iexact=query) |
            Q(email__iexact=query)
        ).distinct()

        if not user_qs.exists() and user_qs.count() != 1:
            raise forms.ValidationError("Invalid credentials")

        user_obj = user_qs.first()

        if not user_obj.check_password(password):
            raise forms.ValidationError("Invalid credentials")

        # if not user_obj.is_active():
        #     raise forms.ValidationError("Inactive user")

        self.cleaned_data['user_obj'] = user_obj

        return super(UserLoginForm, self).clean(*args, **kwargs)

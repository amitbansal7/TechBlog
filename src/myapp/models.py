from django.db import models

POST_CHOICES = (
    ('post', 'Post'),
    ('draft', 'Draft'),
)

TAG_CHOICES = (
    ('one', 'One'),
    ('two', 'Two'),
)


class Post(models.Model):
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100, choices=TAG_CHOICES)
    content = models.TextField()
    post_status = models.CharField(max_length=1000, choices=POST_CHOICES)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Created on:')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('myapp.Post', related_name='comments')
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    byadmin = models.BooleanField(default=False)

    def __str__(self):
        return ("{author}, {email}".format(author=self.author, email=self.email))
from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(verbose_name='username', max_length=50, blank=True, null=True)
    password = models.CharField(verbose_name='Password', max_length=50, blank=True, null=True)
    is_active = models.BooleanField(verbose_name=('Active'), default=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Post (models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now()
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comment(self):
        return self.comments.filter(approved_comment=True)

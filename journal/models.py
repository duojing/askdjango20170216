from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model): #상속받기
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('journal:post_list', args=[self.pk])


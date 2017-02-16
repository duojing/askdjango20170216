from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, related_name = 'shop_post_set')

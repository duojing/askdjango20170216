# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-02 02:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_post_tag_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='blog_post_set', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
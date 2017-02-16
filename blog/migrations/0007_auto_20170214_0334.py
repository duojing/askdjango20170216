# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-14 03:34
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='포스팅 제목으로 노출됩니다. 최대 100자까지 지원됩니다.', max_length=100, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='제목'),
        ),
    ]
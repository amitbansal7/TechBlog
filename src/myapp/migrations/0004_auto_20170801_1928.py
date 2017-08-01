# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 13:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_comment_byadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(choices=[('algorithms', 'Algorithms'), ('django', 'Django')], max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20170721_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='byadmin',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20170801_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hits',
            field=models.BigIntegerField(default=0),
        ),
    ]

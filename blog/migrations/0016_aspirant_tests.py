# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-30 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20181030_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='aspirant',
            name='tests',
            field=models.ManyToManyField(blank=True, null=True, related_name='aspirants', to='blog.Test'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-29 14:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_aspirant_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aspirant',
            name='tests',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_hierarchy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aspirants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('hierarchy', models.IntegerField(default=1)),
            ],
        ),
    ]

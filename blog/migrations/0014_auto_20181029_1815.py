# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-29 15:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_aspirant_tests'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intresting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('kurator', models.TextField(default=1)),
                ('diser_name', models.TextField(default=1)),
                ('text', models.TextField()),
                ('hierarchy', models.IntegerField(default=1)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='aspirant',
            name='intrestings',
            field=models.ManyToManyField(related_name='aspirants', to='blog.Intresting'),
        ),
    ]

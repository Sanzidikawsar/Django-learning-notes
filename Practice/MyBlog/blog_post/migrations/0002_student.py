# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('s_id', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=1)),
                ('varsity', models.CharField(max_length=50)),
            ],
        ),
    ]

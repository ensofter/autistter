# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-20 12:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autist', '0024_auto_20180120_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addproject',
            name='account',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-20 11:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autist', '0020_auto_20180119_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addproject',
            name='account',
        ),
    ]

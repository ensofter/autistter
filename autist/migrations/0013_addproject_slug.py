# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-18 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autist', '0012_auto_20180118_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproject',
            name='slug',
            field=models.CharField(blank=True, max_length=200, verbose_name='Транслит'),
        ),
    ]

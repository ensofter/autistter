# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-22 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autist', '0054_auto_20180322_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, max_length=250, verbose_name='Alias'),
        ),
    ]

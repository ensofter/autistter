# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-20 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autist', '0022_addproject_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproject',
            name='account',
            field=models.CharField(max_length=1),
        ),
    ]

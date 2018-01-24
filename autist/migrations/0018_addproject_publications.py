# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-19 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('autist', '0017_delete_socialpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproject',
            name='publications',
            field=models.ManyToManyField(to='socialaccount.SocialAccount'),
        ),
    ]

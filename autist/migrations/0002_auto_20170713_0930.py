# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 09:30
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
    ]

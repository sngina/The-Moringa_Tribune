# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-06-30 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(null=True, upload_to='articles/'),
        ),
    ]

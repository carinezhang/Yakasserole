# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-27 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170527_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recette',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=b'images', verbose_name=b'Image'),
        ),
    ]

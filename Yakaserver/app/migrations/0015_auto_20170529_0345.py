# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-29 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20170529_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recette',
            name='picture',
            field=models.ImageField(default=b'/static/app/images/default.png', upload_to=b'/static/app/images/'),
        ),
    ]

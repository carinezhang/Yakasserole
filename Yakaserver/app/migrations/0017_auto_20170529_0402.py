# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-29 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20170529_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recette',
            name='picture',
            field=models.CharField(blank=True, default=b'/static/app/images/default.png', max_length=300),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-29 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20170529_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recette',
            name='picture',
            field=models.CharField(max_length=300),
        ),
    ]

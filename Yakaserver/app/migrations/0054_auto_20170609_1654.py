# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-09 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0053_auto_20170609_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atelier',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='atelier',
            name='time',
            field=models.TimeField(),
        ),
    ]

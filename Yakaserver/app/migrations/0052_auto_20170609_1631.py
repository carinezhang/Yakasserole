# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-09 16:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0051_auto_20170609_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atelier',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 6, 9, 16, 31, 5, 472825)),
        ),
        migrations.AlterField(
            model_name='atelier',
            name='duration',
            field=models.TimeField(default=0),
        ),
        migrations.AlterField(
            model_name='atelier',
            name='time',
            field=models.TimeField(default=datetime.datetime(2017, 6, 9, 16, 31, 5, 472865, tzinfo=utc)),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-09 00:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_auto_20170609_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atelier',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 6, 9, 2, 10, 40, 866000)),
        ),
        migrations.AlterField(
            model_name='atelier',
            name='time',
            field=models.TimeField(default=datetime.datetime(2017, 6, 9, 0, 10, 40, 866000, tzinfo=utc)),
        ),
    ]

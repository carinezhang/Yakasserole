# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-06 13:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20170606_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atelier',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 6, 6, 15, 59, 44, 682000)),
        ),
        migrations.AlterField(
            model_name='atelier',
            name='time',
            field=models.TimeField(default=datetime.datetime(2017, 6, 6, 13, 59, 44, 682000, tzinfo=utc)),
        ),
    ]

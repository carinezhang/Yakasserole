# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-09 09:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_auto_20170609_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atelier',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 6, 9, 11, 6, 39, 44000)),
        ),
        migrations.AlterField(
            model_name='atelier',
            name='time',
            field=models.TimeField(default=datetime.datetime(2017, 6, 9, 9, 6, 39, 44000, tzinfo=utc)),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-08 22:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20170606_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atelier',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 6, 9, 0, 59, 56, 93000)),
        ),
        migrations.AlterField(
            model_name='atelier',
            name='time',
            field=models.TimeField(default=datetime.datetime(2017, 6, 8, 22, 59, 56, 93000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='recette',
            name='picture',
            field=models.ImageField(default=b'app/images/default.png', upload_to=b'app/images/'),
        ),
    ]

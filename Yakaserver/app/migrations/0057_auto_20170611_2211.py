# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-11 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0056_merge_20170609_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atelier',
            name='place',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='atelier',
            name='restant',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='atelierinscription',
            name='nbplace',
            field=models.IntegerField(),
        ),
    ]

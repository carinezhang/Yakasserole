# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-29 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20170529_0414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recette',
            name='comments',
            field=models.ManyToManyField(to='app.Comment'),
        ),
    ]
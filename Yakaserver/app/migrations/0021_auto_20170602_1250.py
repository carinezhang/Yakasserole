# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-02 12:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0020_auto_20170529_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atelier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('place', models.DecimalField(decimal_places=0, default=0, max_digits=15)),
                ('lieu', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AtelierComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recette',
            name='ingredients',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recette',
            name='recetteDetail',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='atelier',
            name='comments',
            field=models.ManyToManyField(to='app.AtelierComment'),
        ),
    ]
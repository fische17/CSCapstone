# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 05:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0004_auto_20161129_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='university_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UniversitiesApp.University'),
        ),
    ]

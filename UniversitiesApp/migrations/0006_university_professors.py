# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0004_auto_20161208_0044'),
        ('UniversitiesApp', '0005_auto_20161114_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='professors',
            field=models.ManyToManyField(to='AuthenticationApp.Teacher'),
        ),
    ]
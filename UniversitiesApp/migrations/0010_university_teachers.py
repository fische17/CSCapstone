# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0006_auto_20161208_0519'),
        ('UniversitiesApp', '0009_remove_university_professors'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='teachers',
            field=models.ManyToManyField(related_name='teachers', to='AuthenticationApp.Teacher'),
        ),
    ]

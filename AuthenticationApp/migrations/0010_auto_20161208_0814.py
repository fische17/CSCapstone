# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 08:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0009_auto_20161208_0812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engineer',
            name='is_engineer',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_teacher',
        ),
    ]

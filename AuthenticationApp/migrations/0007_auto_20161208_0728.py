# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 07:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0006_auto_20161208_0519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='is_professor',
            new_name='is_teacher',
        ),
    ]

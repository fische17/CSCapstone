# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CompaniesApp', '0002_auto_20161114_1759'),
        ('AuthenticationApp', '0013_merge_20161208_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineer',
            name='company',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='CompaniesApp.Company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='languages',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GroupsApp', '0001_initial'),
        ('CommentsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GroupsApp.Group'),
        ),
    ]

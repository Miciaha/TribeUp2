# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-22 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_remove_buildinfo_build_event_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildinfo',
            name='build_month_string',
            field=models.CharField(default='Null', max_length=8),
            preserve_default=False,
        ),
    ]
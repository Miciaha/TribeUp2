# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-22 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_event_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_link',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-09-04 02:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0142_auto_20200904_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apiarysite',
            name='proposal_apiary_ids',
        ),
    ]

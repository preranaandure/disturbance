# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-07-07 02:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0104_auto_20200707_0914'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='annualrentalfeeperiod',
            unique_together=set([('period_start_date', 'period_end_date')]),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-07-18 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0112_auto_20200716_1305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apiaryannualrentalfeerundate',
            options={'verbose_name': 'Annual Site Fee Issue Date'},
        ),
        migrations.AlterField(
            model_name='apiaryannualrentalfeerundate',
            name='name',
            field=models.CharField(choices=[('date_to_run_cron_job', 'Date to Issue')], max_length=50, unique=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-10-06 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0309_auto_20230912_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dasmaplayer',
            name='display_name',
            field=models.CharField(default='dummy', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dasmaplayer',
            name='layer_name',
            field=models.CharField(default='dummy', max_length=200),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-10-05 02:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0181_auto_20201002_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approval',
            name='apiary_renewal_document',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-02-27 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0291_merge_20220701_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spatialqueryquestion',
            name='answer_mlq',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Answer (Masterlist Question)'),
        ),
    ]
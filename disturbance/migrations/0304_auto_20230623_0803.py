# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-06-23 00:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0303_auto_20230613_1333'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='spatialqueryquestion',
            unique_together=set([('question', 'answer_mlq')]),
        ),
    ]
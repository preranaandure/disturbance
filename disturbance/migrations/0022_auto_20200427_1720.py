# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-04-27 09:20
from __future__ import unicode_literals

import disturbance.components.compliances.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0021_auto_20200427_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='fee_invoice_reference',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='compliancedocument',
            name='_file',
            field=models.FileField(max_length=500, upload_to=disturbance.components.compliances.models.update_proposal_complaince_filename),
        ),
    ]

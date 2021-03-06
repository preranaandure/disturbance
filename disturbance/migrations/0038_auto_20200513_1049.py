# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-05-13 02:49
from __future__ import unicode_literals

import disturbance.components.compliances.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0037_auto_20200513_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compliancedocument',
            name='_file',
            field=models.FileField(max_length=500, upload_to=disturbance.components.compliances.models.update_proposal_complaince_filename),
        ),
        migrations.AlterField(
            model_name='sitecategory',
            name='name',
            field=models.CharField(choices=[('south_west', 'South West'), ('remote', 'Remote')], max_length=50, unique=True),
        ),
    ]

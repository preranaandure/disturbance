# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-05-12 07:46
from __future__ import unicode_literals

import disturbance.components.compliances.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0032_auto_20200512_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteapplicationfee',
            name='site_category',
        ),
        migrations.AlterField(
            model_name='compliancedocument',
            name='_file',
            field=models.FileField(max_length=500, upload_to=disturbance.components.compliances.models.update_proposal_complaince_filename),
        ),
        migrations.DeleteModel(
            name='SiteApplicationFee',
        ),
    ]

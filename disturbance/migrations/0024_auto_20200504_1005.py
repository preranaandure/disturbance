# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-05-04 02:05
from __future__ import unicode_literals

import disturbance.components.compliances.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0023_auto_20200427_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiarySite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_guid', models.CharField(blank=True, max_length=30)),
                ('proposal_apiary_site_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='disturbance.ProposalApiarySiteLocation')),
            ],
        ),
        migrations.AlterField(
            model_name='compliancedocument',
            name='_file',
            field=models.FileField(max_length=500, upload_to=disturbance.components.compliances.models.update_proposal_complaince_filename),
        ),
        migrations.AlterField(
            model_name='proposaltype',
            name='name',
            field=models.CharField(choices=[('Disturbance', 'Disturbance'), ('Powerline Maintenance', 'Powerline Maintenance'), ('Apiary', 'Apiary')], default='Disturbance', max_length=64, verbose_name='Application name (eg. Disturbance, Apiary)'),
        ),
    ]

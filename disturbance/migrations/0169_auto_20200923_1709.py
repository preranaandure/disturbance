# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-09-23 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0168_apiarysiteonapproval_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiarysite',
            name='approval_link_for_vacant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacant_apiary_site', to='disturbance.ApiarySiteOnApproval'),
        ),
        migrations.AddField(
            model_name='apiarysite',
            name='proposal_link_for_vacant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacant_apiary_site', to='disturbance.ApiarySiteOnProposal'),
        ),
    ]

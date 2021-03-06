# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-06-12 03:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0076_approval_proxy_applicant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='proxy_applicant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='disturbance_proxy_approvals', to=settings.AUTH_USER_MODEL),
        ),
    ]

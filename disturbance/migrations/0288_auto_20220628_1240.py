# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-06-28 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0287_auto_20220628_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiaryannualrentalfeerundate',
            name='enabled',
            field=models.BooleanField(default=False, help_text='Sets whether the annual fee is applied to the sites by the cron job', verbose_name='Apply by cronjob'),
        ),
        migrations.AlterField(
            model_name='apiaryannualrentalfeerundate',
            name='enabled_for_new_site',
            field=models.BooleanField(default=False, help_text='Sets whether the annual fee is applied when an application is approved', verbose_name='Apply when approved'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-05 06:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0072_applicationcondition_licence_activity_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('condition', models.TextField(blank=True, null=True)),
                ('licence_activity_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wildlifecompliance.WildlifeLicenceActivityType')),
            ],
        ),
        migrations.AddField(
            model_name='applicationcondition',
            name='default_condition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wildlifecompliance.DefaultCondition'),
        ),
    ]
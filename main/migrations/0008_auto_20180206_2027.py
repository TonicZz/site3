# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-06 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_tipinstr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='tip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.TipInstr'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-08 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_auto_20200130_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='texts',
            field=models.TextField(),
        ),
    ]
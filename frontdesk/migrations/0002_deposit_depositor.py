# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontdesk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='depositor',
            field=models.CharField(default='gn1', max_length=16),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-02-01 08:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artical',
            new_name='Article',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 11:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20161005_0556'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippet',
            options={'permissions': (('view_snippet', 'View Snippet'), ('edit_snippet', 'Edit Snippet'))},
        ),
    ]
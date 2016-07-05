# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kunden',
            name='aktiv',
            field=models.CharField(default=0, choices=[('1', 'Eingecheckt'), ('0', 'nicht Eingecheckt')], max_length=4),
            preserve_default=False,
        ),
    ]

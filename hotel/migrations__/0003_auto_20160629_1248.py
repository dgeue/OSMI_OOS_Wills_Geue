# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20160628_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kunden',
            name='kunden_id',
        ),
        migrations.AlterField(
            model_name='zimmer',
            name='max_betten',
            field=models.IntegerField(verbose_name='Anzahl max. Betten'),
        ),
    ]

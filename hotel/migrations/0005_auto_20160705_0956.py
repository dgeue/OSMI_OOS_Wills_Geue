# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_auto_20160705_0931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zimmer',
            old_name='id',
            new_name='zimmer_id',
        ),
        migrations.AlterField(
            model_name='buchung',
            name='zimmer_id',
            field=models.ForeignKey(to='hotel.zimmer'),
        ),
    ]

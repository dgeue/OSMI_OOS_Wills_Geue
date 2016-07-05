# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_auto_20160629_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zimmer',
            old_name='zimmer_id',
            new_name='id',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_kunden_aktiv'),
    ]

    operations = [
        migrations.AddField(
            model_name='zimmer',
            name='image',
            field=models.ImageField(upload_to='static/images/', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buchung',
            name='zimmer_id',
            field=models.IntegerField(verbose_name='Zimmernummer'),
        ),
    ]

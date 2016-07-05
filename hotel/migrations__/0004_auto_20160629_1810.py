# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_auto_20160629_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zimmer',
            name='id',
        ),
        migrations.AddField(
            model_name='zimmer',
            name='zimmer_id',
            field=models.AutoField(serialize=False, primary_key=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buchung',
            name='anzahl_tage',
            field=models.IntegerField(verbose_name='Anzahl der zu buchenden Tage'),
        ),
        migrations.AlterField(
            model_name='kunden',
            name='zimmer',
            field=models.IntegerField(verbose_name='Zimmernummer'),
        ),
        migrations.AlterField(
            model_name='zimmer',
            name='preis',
            field=models.IntegerField(verbose_name='Zimmerpreis in Euro pro Nacht'),
        ),
        migrations.AlterField(
            model_name='zimmer',
            name='status',
            field=models.CharField(choices=[('0', 'Buchbar'), ('1', 'nicht Buchbar')], max_length=4),
        ),
    ]

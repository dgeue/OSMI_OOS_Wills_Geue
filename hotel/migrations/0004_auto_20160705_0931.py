# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_auto_20160701_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buchung',
            name='datum_bis',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='buchung',
            name='datum_von',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='zimmer',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='zimmer',
            name='status',
            field=models.CharField(max_length=4, choices=[('ja', 'Buchbar'), ('nein', 'nicht Buchbar')]),
        ),
    ]

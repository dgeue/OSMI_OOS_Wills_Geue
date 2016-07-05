# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_auto_20160705_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kunden',
            name='zimmer',
            field=models.ForeignKey(to='hotel.zimmer'),
        ),
        migrations.AlterField(
            model_name='zimmer',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='kunden',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('kunden_id', models.IntegerField()),
                ('vorname', models.TextField(verbose_name='Vorname')),
                ('nachname', models.TextField(verbose_name='Nachname')),
                ('zimmer', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='zimmer',
            name='max_betten',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

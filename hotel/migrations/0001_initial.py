# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buchung',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('zimmer_id', models.IntegerField()),
                ('nutzer', models.TextField(verbose_name='Nutzername')),
                ('anzahl_tage', models.IntegerField(verbose_name='Anzahl der zu buchenden Tage')),
                ('datum_von', models.DateTimeField()),
                ('datum_bis', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='kunden',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('vorname', models.TextField(verbose_name='Vorname')),
                ('nachname', models.TextField(verbose_name='Nachname')),
                ('zimmer', models.IntegerField(verbose_name='Zimmernummer')),
            ],
        ),
        migrations.CreateModel(
            name='zimmer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('zimmer', models.TextField(verbose_name='Zimmername')),
                ('preis', models.IntegerField(verbose_name='Zimmerpreis in Euro pro Nacht')),
                ('status', models.CharField(max_length=4, choices=[('0', 'Buchbar'), ('1', 'nicht Buchbar')])),
                ('max_betten', models.IntegerField(verbose_name='Anzahl max. Betten')),
            ],
        ),
    ]

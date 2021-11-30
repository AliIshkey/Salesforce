# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-22 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Salutation', models.CharField(choices=[(b'Mr', b'Mr'), (b'Mrs.', b'Mrs'), (b'Ms', b'Ms')], max_length=9)),
                ('FirstName', models.CharField(blank=True, max_length=255, null=True)),
                ('LastName', models.CharField(max_length=255)),
                ('Title', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255, unique=True)),
                ('Phone', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]

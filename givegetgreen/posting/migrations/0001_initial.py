# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('item_category', models.CharField(max_length=100)),
                ('item_description', models.CharField(max_length=100)),
            ],
        ),
    ]

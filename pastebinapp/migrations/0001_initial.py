# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(choices=[('C', 'C'), ('CPP', 'C++'), ('RUST', 'RUST'), ('PYTHON', 'PYTHON')], default='PYTHON', max_length=20000)),
            ],
        ),
    ]

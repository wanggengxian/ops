# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-24 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('idcs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('idc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idcs.Idc', verbose_name='所在机房')),
            ],
            options={
                'db_table': 'resources_cabinet',
                'ordering': ['id'],
            },
        ),
    ]

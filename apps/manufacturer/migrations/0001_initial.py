# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-14 09:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(db_index=True, help_text='厂商名称', max_length=32, unique=True, verbose_name='厂商名称')),
                ('tel', models.CharField(help_text='联系电话', max_length=15, null=True, verbose_name='联系电话')),
                ('mail', models.CharField(help_text='联系邮件', max_length=32, null=True, verbose_name='联系邮件')),
                ('remark', models.CharField(help_text='备注', max_length=300, null=True, verbose_name='备注')),
            ],
            options={
                'db_table': 'resources_manufacturer',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(help_text='型号名称', max_length=20, verbose_name='型号名称')),
                ('vendor', models.ForeignKey(help_text='所属制造商', on_delete=django.db.models.deletion.CASCADE, to='manufacturer.Manufacturer', verbose_name='所属制造商')),
            ],
            options={
                'db_table': 'resources_productmodel',
                'ordering': ['id'],
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-11 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manufacturer', '0001_initial'),
        ('idcs', '0002_auto_20190711_1341'),
        ('cabinet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_addr', models.CharField(db_index=True, help_text='ip地址', max_length=15, unique=True, verbose_name='ip地址')),
                ('netmask', models.CharField(help_text='子网掩码', max_length=15, verbose_name='子网掩码')),
                ('remark', models.CharField(help_text='备注', max_length=200, null=True, verbose_name='备注')),
            ],
            options={
                'db_table': 'resources_ip',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='网卡设备名', max_length=20, verbose_name='网卡设备名')),
                ('mac_address', models.CharField(help_text='MAC地址', max_length=30, verbose_name='MAC地址')),
                ('remark', models.CharField(help_text='备注', max_length=200, null=True, verbose_name='备注')),
            ],
            options={
                'db_table': 'resources_network_device',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(db_index=True, help_text='管理ip', max_length=15, unique=True, verbose_name='管理ip')),
                ('hostname', models.CharField(db_index=True, help_text='主机名', max_length=20, unique=True, verbose_name='主机名')),
                ('cpu', models.CharField(help_text='CPU', max_length=50, verbose_name='CPU')),
                ('mem', models.CharField(help_text='内存', max_length=32, verbose_name='内存')),
                ('disk', models.CharField(help_text='磁盘', max_length=200, verbose_name='磁盘')),
                ('os', models.CharField(help_text='OS', max_length=50, verbose_name='OS')),
                ('sn', models.CharField(db_index=True, help_text='SN', max_length=50, verbose_name='SN')),
                ('rmt_card_ip', models.CharField(db_index=True, help_text='管理管理卡IP', max_length=15, unique=True, verbose_name='管理管理卡IP')),
                ('cabinet_position', models.CharField(help_text='机柜内位置', max_length=20, null=True, verbose_name='机柜内位置')),
                ('uuid', models.CharField(db_index=True, help_text='UUID', max_length=50, unique=True, verbose_name='UUID')),
                ('last_check', models.DateTimeField(auto_now=True, db_index=True, help_text='检测时间', verbose_name='检测时间')),
                ('remark', models.CharField(help_text='备注', max_length=200, null=True, verbose_name='备注')),
                ('cabinet', models.ForeignKey(help_text='所在机柜', null=True, on_delete=django.db.models.deletion.CASCADE, to='cabinet.Cabinet', verbose_name='所在机柜')),
                ('idc', models.ForeignKey(help_text='所在机房', null=True, on_delete=django.db.models.deletion.CASCADE, to='idcs.Idc', verbose_name='所在机房')),
                ('manufacturer', models.ForeignKey(help_text='制造商', on_delete=django.db.models.deletion.CASCADE, to='manufacturer.Manufacturer', verbose_name='制造商')),
                ('model_name', models.ForeignKey(help_text='服务器型号', on_delete=django.db.models.deletion.CASCADE, to='manufacturer.ProductModel', verbose_name='服务型号')),
            ],
            options={
                'db_table': 'resources_server',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='host',
            field=models.ForeignKey(help_text='所在服务器', on_delete=django.db.models.deletion.CASCADE, to='servers.Server', verbose_name='所在服务器'),
        ),
        migrations.AddField(
            model_name='ip',
            name='device',
            field=models.ForeignKey(help_text='所在网卡', on_delete=django.db.models.deletion.CASCADE, to='servers.NetworkDevice', verbose_name='所在网卡'),
        ),
    ]

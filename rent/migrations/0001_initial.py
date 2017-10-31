# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-10-30 16:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('community_name', models.CharField(max_length=100)),
                ('house_type', models.CharField(max_length=20)),
                ('house_number', models.IntegerField()),
                ('hourse_tel', models.CharField(max_length=15)),
                ('is_rent', models.BooleanField()),
                ('house_create', models.DateTimeField(auto_now_add=True)),
                ('house_update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('llord_nickname', models.CharField(max_length=10)),
                ('llord_name', models.CharField(max_length=5)),
                ('llord_ID', models.CharField(max_length=20)),
                ('llord_tel', models.CharField(max_length=15)),
                ('llord_uid', models.IntegerField(unique=True)),
                ('llord_password', models.CharField(max_length=64, unique=True)),
                ('llord_create', models.DateTimeField(auto_now_add=True)),
                ('llord_update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rentneed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_addr', models.CharField(max_length=50)),
                ('scope', models.IntegerField(max_length=20)),
                ('rental', models.IntegerField(max_length=20)),
                ('area', models.IntegerField(max_length=20)),
                ('number', models.IntegerField(max_length=20)),
                ('story', models.IntegerField(max_length=20)),
                ('rent_type', models.CharField(max_length=20)),
                ('rent_create', models.DateTimeField(auto_now_add=True)),
                ('rent_update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=20)),
                ('userid', models.CharField(max_length=15)),
                ('birth', models.DateTimeField()),
                ('sex', models.CharField(max_length=5)),
                ('tel', models.CharField(max_length=15)),
                ('uid', models.IntegerField(unique=True)),
                ('user_create', models.DateTimeField(auto_now_add=True)),
                ('user_update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='llord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.Landlord'),
        ),
    ]
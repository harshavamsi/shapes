# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ACM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('para1', models.TextField()),
                ('para2', models.TextField()),
                ('para3', models.TextField()),
                ('image1', models.ImageField(blank=True, upload_to=b'')),
                ('image2', models.ImageField(blank=True, upload_to=b'')),
                ('head1', models.CharField(max_length=120)),
                ('head2', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=125)),
                ('phone', models.BigIntegerField()),
                ('messege', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=125)),
                ('phone', models.BigIntegerField()),
                ('messege', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='dance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('para1', models.TextField()),
                ('para2', models.TextField()),
                ('para3', models.TextField()),
                ('image1', models.ImageField(blank=True, upload_to=b'')),
                ('image2', models.ImageField(blank=True, upload_to=b'')),
                ('head1', models.CharField(max_length=120)),
                ('head2', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=125)),
                ('phone', models.BigIntegerField()),
                ('messege', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='IEEE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('para1', models.TextField()),
                ('para2', models.TextField()),
                ('para3', models.TextField()),
                ('image1', models.ImageField(blank=True, upload_to=b'')),
                ('image2', models.ImageField(blank=True, upload_to=b'')),
                ('head1', models.CharField(max_length=120)),
                ('head2', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=125)),
                ('phone', models.BigIntegerField()),
                ('messege', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('para1', models.TextField()),
                ('para2', models.TextField()),
                ('para3', models.TextField()),
                ('image1', models.ImageField(blank=True, upload_to=b'')),
                ('image2', models.ImageField(blank=True, upload_to=b'')),
                ('head1', models.CharField(max_length=120)),
                ('head2', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=125)),
                ('phone', models.BigIntegerField()),
                ('messege', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='sankalp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('para1', models.TextField()),
                ('para2', models.TextField()),
                ('para3', models.TextField()),
                ('image1', models.ImageField(blank=True, upload_to=b'')),
                ('image2', models.ImageField(blank=True, upload_to=b'')),
                ('head1', models.CharField(max_length=120)),
                ('head2', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=125)),
                ('phone', models.BigIntegerField()),
                ('messege', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='theatre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('para1', models.TextField()),
                ('para2', models.TextField()),
                ('para3', models.TextField()),
                ('image1', models.ImageField(blank=True, upload_to=b'')),
                ('image2', models.ImageField(blank=True, upload_to=b'')),
                ('head1', models.CharField(max_length=120)),
                ('head2', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=125)),
                ('phone', models.BigIntegerField()),
                ('messege', models.TextField()),
            ],
        ),
    ]
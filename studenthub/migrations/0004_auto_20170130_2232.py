# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-30 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studenthub', '0003_auto_20170130_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='acmContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=125)),
                ('phone', models.BigIntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='danceContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=125)),
                ('phone', models.BigIntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ieeeContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=125)),
                ('phone', models.BigIntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='musicContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=125)),
                ('phone', models.BigIntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='quizContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=125)),
                ('phone', models.BigIntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='sankalpContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=125)),
                ('phone', models.BigIntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='theatreContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=125)),
                ('phone', models.BigIntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='acm',
            name='email',
        ),
        migrations.RemoveField(
            model_name='acm',
            name='message',
        ),
        migrations.RemoveField(
            model_name='acm',
            name='name',
        ),
        migrations.RemoveField(
            model_name='acm',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='dance',
            name='email',
        ),
        migrations.RemoveField(
            model_name='dance',
            name='message',
        ),
        migrations.RemoveField(
            model_name='dance',
            name='name',
        ),
        migrations.RemoveField(
            model_name='dance',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='ieee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='ieee',
            name='message',
        ),
        migrations.RemoveField(
            model_name='ieee',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ieee',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='music',
            name='email',
        ),
        migrations.RemoveField(
            model_name='music',
            name='message',
        ),
        migrations.RemoveField(
            model_name='music',
            name='name',
        ),
        migrations.RemoveField(
            model_name='music',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='email',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='message',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='name',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='sankalp',
            name='email',
        ),
        migrations.RemoveField(
            model_name='sankalp',
            name='message',
        ),
        migrations.RemoveField(
            model_name='sankalp',
            name='name',
        ),
        migrations.RemoveField(
            model_name='sankalp',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='theatre',
            name='email',
        ),
        migrations.RemoveField(
            model_name='theatre',
            name='message',
        ),
        migrations.RemoveField(
            model_name='theatre',
            name='name',
        ),
        migrations.RemoveField(
            model_name='theatre',
            name='phone',
        ),
    ]

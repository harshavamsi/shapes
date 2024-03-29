# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-31 16:03
from __future__ import unicode_literals

from django.db import migrations, models
import studenthub.models


class Migration(migrations.Migration):

    dependencies = [
        ('studenthub', '0007_auto_20170131_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acm',
            name='image1',
            field=models.ImageField(blank=True, upload_to=studenthub.models.update_image_name),
        ),
        migrations.AlterField(
            model_name='acm',
            name='image2',
            field=models.ImageField(blank=True, upload_to=studenthub.models.update_image_name),
        ),
        migrations.AlterField(
            model_name='dance',
            name='image1',
            field=models.ImageField(blank=True, upload_to=studenthub.models.update_image_name),
        ),
        migrations.AlterField(
            model_name='dance',
            name='image2',
            field=models.ImageField(blank=True, upload_to=studenthub.models.update_image_name),
        ),
        migrations.AlterField(
            model_name='ieee',
            name='image1',
            field=models.ImageField(blank=True, upload_to=studenthub.models.update_image_name),
        ),
        migrations.AlterField(
            model_name='ieee',
            name='image2',
            field=models.ImageField(blank=True, upload_to=studenthub.models.update_image_name),
        ),
        migrations.AlterField(
            model_name='music',
            name='image1',
            field=models.ImageField(blank=True, upload_to=studenthub.models.update_image_name),
        ),
        migrations.AlterField(
            model_name='music',
            name='image2',
            field=models.ImageField(blank=True, upload_to=studenthub.models.update_image_name),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='image1',
            field=models.ImageField(blank=True, upload_to=studenthub.models.update_image_name),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='image2',
            field=models.ImageField(blank=True, upload_to=studenthub.models.update_image_name),
        ),
        migrations.AlterField(
            model_name='sankalp',
            name='image1',
            field=models.ImageField(blank=True, upload_to=studenthub.models.update_image_name),
        ),
        migrations.AlterField(
            model_name='sankalp',
            name='image2',
            field=models.ImageField(blank=True, upload_to=studenthub.models.update_image_name),
        ),
        migrations.AlterField(
            model_name='theatre',
            name='image1',
            field=models.ImageField(blank=True, upload_to=studenthub.models.update_image_name),
        ),
        migrations.AlterField(
            model_name='theatre',
            name='image2',
            field=models.ImageField(blank=True, upload_to=studenthub.models.update_image_name),
        ),
    ]

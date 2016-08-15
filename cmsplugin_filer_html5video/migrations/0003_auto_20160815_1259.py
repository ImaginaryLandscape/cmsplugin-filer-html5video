# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_html5video', '0002_auto_20160815_1134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filerhtml5video',
            options={'verbose_name': 'filer html5 video'},
        ),
        migrations.AlterField(
            model_name='filerhtml5video',
            name='alignment',
            field=models.CharField(blank=True, choices=[(b'left', 'Left'), (b'right', 'Right'), (b'center', 'Center')], max_length=10, null=True, verbose_name='video alignment'),
        ),
        migrations.AlterField(
            model_name='filerhtml5video',
            name='height',
            field=models.PositiveSmallIntegerField(blank=True, default=240, verbose_name='height'),
        ),
        migrations.AlterField(
            model_name='filerhtml5video',
            name='width',
            field=models.PositiveSmallIntegerField(blank=True, default=320, help_text='In pixels. Leave empty for full width.', verbose_name='max width'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0015_auto_20160421_0000'),
        ('filer', '0004_auto_20160328_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerHTML5Video',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(blank=True, default=b'', max_length=100, verbose_name='title')),
                ('width', models.PositiveSmallIntegerField(default=320, verbose_name='width')),
                ('height', models.PositiveSmallIntegerField(default=240, verbose_name='height')),
                ('auto_play', models.BooleanField(default=False, verbose_name='auto play')),
                ('auto_hide', models.BooleanField(default=False, verbose_name='auto hide')),
                ('fullscreen', models.BooleanField(default=True, verbose_name='fullscreen')),
                ('loop', models.BooleanField(default=False, verbose_name='loop')),
                ('image', filer.fields.image.FilerImageField(blank=True, help_text='preview image file', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='filer.Image', verbose_name='image')),
                ('video_mp4', filer.fields.file.FilerFileField(blank=True, help_text='MP4 h264 encoded video file (Safari, Chrome, IE9)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='filer.File', verbose_name='movie file (MP4)')),
                ('video_ogv', filer.fields.file.FilerFileField(blank=True, help_text='ogv encoded video file (Firefox)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='filer.File', verbose_name='movie file (ogv)')),
                ('video_webm', filer.fields.file.FilerFileField(blank=True, help_text='webM encoded video file (Firefox)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='filer.File', verbose_name='movie file (webM)')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

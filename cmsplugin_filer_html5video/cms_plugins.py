# -*- coding: utf-8 -*-

import os

from django.utils.translation import ugettext_lazy as _
from django.templatetags.static import static

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from cmsplugin_filer_html5video.models import FilerHTML5Video

class FilerHTML5VideoPlugin(CMSPluginBase):
    model = FilerHTML5Video
    module = "Filer"
    name = _("HTML5 Video")

    render_template = "cmsplugin_filer_html5video/video.html"
    text_enabled = True


    fieldsets = [
        (None, {
            'fields': (
                'video_url',
                'alignment',
                'width',
             )
        }),
        (_('Uploaded Video'), {
            'classes': ('collapse',),
            'fields': (
                'video_mp4', 
                'video_webm', 
                'video_ogv', 
                'auto_play',
                'auto_hide',
                'fullscreen',
                'loop',
            )
        })
    ]

    def render(self, context, instance, placeholder):
        formats = {}
        for format in ('video_mp4', 'video_webm', 'video_ogv'):
            if getattr(instance, format + '_id'):
                formats[format.replace('_', '/')] = getattr(instance, format).url
        context.update({
            'object': instance,
            'placeholder':placeholder,
            'formats': formats
        })
        return context

    def icon_src(self, instance):
        return static("filer/icons/video_%sx%s.png" % (32, 32,))

plugin_pool.register_plugin(FilerHTML5VideoPlugin)

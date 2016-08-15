# -*- coding: utf-8 -*-

from cms.models import CMSPlugin
from cmsplugin_filer_html5video import plugin_settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField

class FilerHTML5Video(CMSPlugin):
    # player settings
    FLOAT_CHOICES = (
        ('left', _("Left")),
        ('right', _("Right")),
        ('center', _("Center")),
    )
    
    title = models.CharField(_('title'), blank=True, default='', max_length=100)
    video_url = models.CharField(_("Video URL"), blank=True, max_length=255,
        help_text="Link to the youtube or vimeo page. Example: "
        "https://www.youtube.com/watch?v=12345678")
    alignment = models.CharField(_("video alignment"), max_length=10, blank=True, null=True, choices=FLOAT_CHOICES)    

    video_mp4  = FilerFileField(verbose_name=_('movie file (MP4)'), help_text=_('MP4 h264 encoded video file (Safari, Chrome, IE9)'), blank=True, null=True, related_name='+')
    video_webm = FilerFileField(verbose_name=_('movie file (webM)'), help_text=_('webM encoded video file (Firefox)'), blank=True, null=True, related_name='+')
    video_ogv = FilerFileField(verbose_name=_('movie file (ogv)'), help_text=_('ogv encoded video file (Firefox)'), blank=True, null=True, related_name='+')
    image = FilerImageField(verbose_name=_('image'), help_text=_('preview image file'), null=True, blank=True, related_name='+')
    width = models.PositiveSmallIntegerField(_('max width'), 
        default=plugin_settings.VIDEO_WIDTH, blank=True, 
        help_text=_('In pixels. Leave empty for full width.'))
    height = models.PositiveSmallIntegerField(_('height'), default=plugin_settings.VIDEO_HEIGHT, blank=True)
    auto_play = models.BooleanField(_('auto play'), default=plugin_settings.VIDEO_AUTOPLAY)
    auto_hide = models.BooleanField(_('auto hide'), default=plugin_settings.VIDEO_AUTOHIDE)
    fullscreen = models.BooleanField(_('fullscreen'), default=plugin_settings.VIDEO_FULLSCREEN)
    loop = models.BooleanField(_('loop'), default=plugin_settings.VIDEO_LOOP)

    class Meta:
        verbose_name = "filer html5 video"

    def __unicode__(self):
        return u"%s" % self.title

    def get_height(self):
        return "%s" % self.height

    def get_width(self):
        return "%s" % self.width


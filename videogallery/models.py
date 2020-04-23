#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import uuid
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class Album(models.Model):
    class Meta(object):
        verbose_name = u"Видеоальбом"
        verbose_name_plural = u"Видеоальбомы"
        ordering = ('-modified',)

    title = models.CharField(max_length=70,
                            verbose_name=u'Название')
    description = models.TextField(max_length=1024,
                                    verbose_name=u'Описание')
    thumb = ProcessedImageField(upload_to='videoalbums',
                                        processors=[ResizeToFit(300)],
                                        format='JPEG', 
                                        options={'quality': 80},
                                        verbose_name=u'Обложка')
    tags = models.CharField(max_length=250,
                            verbose_name=u'Теги')
    is_visible = models.BooleanField(default=True,
                                    verbose_name=u'Видимый')
    created = models.DateTimeField(auto_now_add=True,
                                    verbose_name=u'Дата создания')
    modified = models.DateTimeField(auto_now_add=True,
                                    verbose_name=u'Дата изменения')
    slug = models.SlugField(max_length=50, unique=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class AlbumVideo(models.Model):
	class Meta(object):
		verbose_name = u"Видео"
		verbose_name_plural = u"Видео"
		ordering = ('-created',)

	title = models.CharField(max_length=70,
	                    	verbose_name=u'Название')
	description = models.TextField(max_length=1024,
									verbose_name=u'Описание')
	link = models.URLField(verbose_name=u'Ссылка')
	tags = models.CharField(max_length=250,
							verbose_name=u'Теги')
	album = models.ForeignKey(Album,
							on_delete=models.CASCADE,
							verbose_name=u'Альбом')
	is_visible = models.BooleanField(default=True,
									verbose_name=u'Видимый')
	created = models.DateTimeField(auto_now_add=True,
									verbose_name=u'Дата создания')
	modified = models.DateTimeField(auto_now_add=True,
									verbose_name=u'Дата изменения')
	slug = models.SlugField(max_length=50, unique=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def video_normalize_url(self):
		return self.link.replace('https://youtu.be/','http://www.youtube.com/v/') + '?version=3'

	video_normalize_url.short_description = 'Ссылка для плеера'
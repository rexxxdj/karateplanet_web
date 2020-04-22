#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import uuid
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class Album(models.Model):
    class Meta(object):
        verbose_name = u"Фотоальбом"
        verbose_name_plural = u"Фотоальбомы"
        ordering = ('-modified',)

    title = models.CharField(max_length=70,
                            verbose_name=u'Название')
    description = models.TextField(max_length=1024,
                                    verbose_name=u'Описание')
    thumb = ProcessedImageField(upload_to='albums', 
    							processors=[ResizeToFit(300)], 
    							format='JPEG', 
    							options={'quality': 90}
                                ,verbose_name=u'Обложка')
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

class AlbumImage(models.Model):
    class Meta(object):
        verbose_name = u"Фотография"
        verbose_name_plural = u"Фотографии"
        ordering = ('-created',)

    image = ProcessedImageField(upload_to='albums', 
    							processors=[ResizeToFit(1280)], 
    							format='JPEG', 
    							options={'quality': 70},
                                verbose_name=u'Изображение')
    image_300 = ProcessedImageField(upload_to='albums',
                                        processors=[ResizeToFit(300)],
                                        format='JPEG', 
                                        options={'quality': 80},
                                        verbose_name=u'Фото 300')
    image_100 = ProcessedImageField(upload_to='albums',
                                        processors=[ResizeToFit(100)],
                                        format='JPEG', 
                                        options={'quality': 90},
                                        verbose_name=u'Фото 100')
    album = models.ForeignKey(Album,
                            on_delete=models.CASCADE,
                            verbose_name=u'Альбом')
    created = models.DateTimeField(auto_now_add=True,
                                    verbose_name=u'Дата создания')
    width = models.IntegerField(default=0,
                                verbose_name=u'Ширина')
    height = models.IntegerField(default=0,
                                verbose_name=u'Высота')
    slug = models.SlugField(max_length=70, 
                            default=uuid.uuid4, 
                            editable=False)
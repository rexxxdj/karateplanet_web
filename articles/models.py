from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import PIL
from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust, ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
	class Meta(object):
		verbose_name = u"Статья"
		verbose_name_plural = u"Статьи"


	def get_absolute_url(self):
		return reverse('articles:article_detail',
						args=[self.publish.year,
						self.publish.strftime('%m'),
						self.publish.strftime('%d'),
						self.slug])

	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
		)
	TYPE_CHOICES = (
		('news', 'News'),
		('event', 'Event'),
		)

	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posted')
	image = models.ImageField(
		blank=True,
		verbose_name=u"Баннер",
		null=True)
	image_50_50 =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
            					ResizeToFill(50, 50)], source='image',
            					format='JPEG', options={'quality': 90})
	image_300_200 =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
        						ResizeToFit(300, 200)], source='image',
        						format='JPEG', options={'quality': 90})
	image_640_480 =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
        						ResizeToFit(640, 480)], source='image',
        						format='JPEG', options={'quality': 90})
	image_800_600 =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
        						ResizeToFit(800, 600)], source='image',
        						format='JPEG', options={'quality': 90})
	body = RichTextUploadingField()
	publish = models.DateTimeField(default = timezone.now)
	situation = models.FileField(upload_to='uploads/files/',
								blank=True,
								verbose_name=u"Файл",
								null=True)
	type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='event')
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	
class Meta:
	ordering = ('-publish',)

def __str__(self):
	return self.title

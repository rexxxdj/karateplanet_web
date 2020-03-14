from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):
	def get_absolute_url(self):
		return reverse('karateplanet:article_detail',
						args=[self.publish.year,
						self.publish.strftime('%m'),
						self,publish.strftime('%d'),
						self.slug])

	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
		)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posted')
	body = models.TextField()
	publish = models.DateTimeField(default = timezone.now)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	
class Meta:
	ordering = ('-publish',)

def __str__(self):
	return self.title

from django.db import models

# Create your models here.
class Banner(models.Model):
	class Meta(object):
		verbose_name = u"Баннер"
		verbose_name_plural = u"Баннера"
		ordering = ('-created',)

	def __str__(self):
		return self.title

	STATUS_CHOICES = (
		('on', 'On'),
		('off', 'Off'),
		)
	TYPE_CHOICES = (
		('carousel', 'Carousel'),
		('sponsor', 'Sponsor'),
		('partner', 'Partner'),
		('na', 'N/A'),
		)

	title = models.CharField(max_length=250,
							verbose_name=u'Название')
	image = models.ImageField(blank=True,
								verbose_name=u"Баннер",
								null=True)
	type = models.CharField(max_length=10, 
							choices=TYPE_CHOICES, 
							default='na',
							verbose_name=u'Тип баннера')
	status = models.CharField(max_length=3, 
								choices=STATUS_CHOICES, 
								default='off',
								verbose_name=u'Статус')
	created = models.DateTimeField(auto_now_add=True,
                                    verbose_name=u'Дата создания')
	is_active = models.IntegerField(default=0,
                                    verbose_name=u'Active')
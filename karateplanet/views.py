from django.shortcuts import render

from articles.models import Article
from photogallery.models import AlbumImage
from banners.models import Banner



def index(request):
	articles = Article.objects.filter(status='published').order_by('-publish')[:6] #.filter(status__exact='publish')
	photos = AlbumImage.objects.order_by('-created')[:6]
	carousel = Banner.objects.filter(type='carousel',status = 'on')

	return render(request,
				'index.html',
				context={'articles': articles
						,'photos': photos
						,'carousel': carousel},
				)
from django.shortcuts import render

from articles.models import Article



def index(request):
	articles = Article.objects.filter(status='published').order_by('-publish')[:6] #.filter(status__exact='publish')

	return render(request,
				'index.html',
				context={'articles': articles},
				)
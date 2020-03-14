from django.shortcuts import render, get_object_or_404
from .models import Article


def article_list(request):
	articles = Article.published.all()
	return render(request, 'karateplanet/articles/list.html',{'posts': posts})

def article_detail(request,year,month,day,article):
	article = get_object_or_404(Article, slug = article,
										status = 'published',
										publish_year = year,
										publish_month=month,
										publish_day=day)
	return render(request, 'karateplanet/articles/detail.html', {'article': article})
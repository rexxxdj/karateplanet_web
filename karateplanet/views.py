from django.shortcuts import render

from articles.models import Article



def index(request):
	articles = (
		{'id': 1,
		 'title': u'Кубок Полесья',
		 'description': u'Lorem',
		 'slug': 235,
		 'type': 1,
		 'publish': u'2020.02.02',
		 'image': '../static/img/desk.jpg'},
		{'id': 2,
		 'title': u'Днепр',
		 'description': u'Подоба',
		 'slug': 235,
		 'type': 1,
		 'publish': u'2020.02.02',
		 'image': '../static/img/desk.jpg'},
		 {'id': 3,
		 'title': u'Харьков',
		 'description': u'Подоба',
		 'slug': 235,
		 'type': 1,
		 'publish': u'2020.02.02',
		 'image': '../static/img/building.jpg'},
		 {'id': 4,
		 'title': u'Просто Носвость',
		 'description': u'Подоба',
		 'slug': 235,
		 'type': 0,
		 'publish': u'2020.02.02',
		 'image': '../static/img/building.jpg'},
		 {'id': 5,
		 'title': u'Еще одна новость',
		 'description': u'Подоба',
		 'slug': 235,
		 'type': 0,
		 'publish': u'2020.02.02',
		 'image': '../static/img/desk.jpg'},
		 {'id': 6,
		 'title': u'Снова новость',
		 'description': u'Подоба',
		 'slug': 235,
		 'type': 0,
		 'publish': u'2020.02.02',
		 'image': '../static/img/building.jpg'}
		 )
	#articles = Article.objects.filter(status__exact='publish')

	return render(request,
				'index.html',
				context={'articles': articles},
				)
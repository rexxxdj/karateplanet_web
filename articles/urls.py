from django.conf.urls import url
from django.urls import path
from . import views


app_name ='articles'

urlpatterns = [
	# post views
	path(r'^$', views.article_list, name='article_list'),
	path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
		views.article_detail,
		name='article_detail'),
]
from django.conf.urls import patterns, url
from photo import views

urlpatterns = patterns('photo.views',
	url(r'^album/(?P<pk>\d+)/(full|thumbnails)/$', views.album, name="album"),
	url(r'^image/(?P<pk>\d+)/$', views.image, name="image"),
	url(r'^$', views.main, name='photo_main'),
	)


from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('blog.views',
	url(r'^(?P<pk>\d+)/$',views.post, name='post'),
	url(r"^add_comment/(?P<pk>\d+)/$", views.add_comment, name="add_comment"),
	url(r"^month/(\d+)/(\d+)/$", views.month, name="month"),
	url(r"^delete_comment/(\d+)/$", views.delete_comment, name="delete_comment"),
	url(r"^delete_comment/(\d+)/(\d+)/$", views.delete_comment, name="delete_comment"),
    )
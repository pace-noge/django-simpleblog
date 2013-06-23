from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#url(r'', include('blog.urls', namespace='main')),
    # Examples:
    url(r'^$', 'blog.views.main', name='main'),
    url(r'^post/', include('blog.urls', namespace='post')),
    url(r'^photo/', include('photo.urls', namespace='photo')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)

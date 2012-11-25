from django.conf.urls import patterns, include, url

urlpatterns = patterns('ebootcamp.views',
    #url(r'^$', include('zinnia.urls')),
    #url(r'^about$', 'about'),
    url(r'^$', 'root'),
    (r'^(?P<page_alias>.+?)/$', 'static_page'),
)

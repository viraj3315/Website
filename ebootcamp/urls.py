from django.conf.urls import patterns, include, url

urlpatterns = patterns('ebootcamp.views',
    #url(r'^$', include('zinnia.urls')),
    #url(r'^about$', 'about'),
    (r'^(?P<page_alias>.+?)/$', 'static_page'),
)

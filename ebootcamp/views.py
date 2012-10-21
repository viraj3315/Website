import sys
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404
from sitemanager.models import Page
from django.db.models import Q

def about(request):
    t = loader.get_template('ebootcamp/about.html')
    c = RequestContext(request, {'active_tab' : 'programs'})
    return HttpResponse(t.render(c))

def static_page(request, page_alias):
    pages = Page.objects.filter(
                Q(url=page_alias))
    for page in pages:
        if 'ebootcamp' in page.groups.values_list('name',flat=True):
        	t = loader.get_template('static/user_page.html')
        	c = RequestContext(request, {'head' : page.head, 'body' : page.body})
        	return HttpResponse(t.render(c))
            #return HttpResponse(page.content)
    raise Http404("Page does not exist")

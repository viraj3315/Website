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
    currtitle = "About"
    sidebar_contents=get_sidebar_content()
    for page in pages:
        if 'ebootcamp' in page.groups.values_list('name',flat=True):
            #sidebar_contents = get_sidebar_content(page.title)
        	t = loader.get_template('static/user_page.html')
        	c = RequestContext(request, {'head' : page.head, 'body' : page.body, 'sidebar_entries' : sidebar_contents })
        	return HttpResponse(t.render(c))
            #return HttpResponse(page.content)
    raise Http404("Page does not exist")

def root(request):
    pages = Page.objects.all()
    sidebar_contents=get_sidebar_content()
    for page in pages:
        if 'ebootcamp' in page.groups.values_list('name',flat=True):
            if page.landing == True:
                t = loader.get_template('static/user_page.html')
                c = RequestContext(request, {'head' : page.head, 'body' : page.body, 'sidebar_entries' : sidebar_contents })
                return HttpResponse(t.render(c))
    raise Http404("Page does not exist") 

def get_sidebar_content():
    current_page_title = "About"
    pages = Page.objects.all()
    contents = []
    for page in pages:
        if 'ebootcamp' in page.groups.values_list('name',flat=True):
            link = {}
            link['name'] = page.title
            if page.title == current_page_title:
                link['current'] = True
            else:
                link['current'] = False
            contents.append(link)
    return contents

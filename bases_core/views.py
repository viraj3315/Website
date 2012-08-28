from django.template import RequestContext, loader
from django.http import HttpResponse

def index(request):
    t = loader.get_template('bases_core/index.html')
    c = RequestContext(request, {'active_tab': 'index'})
    return HttpResponse(t.render(c))

def about(request):
    t = loader.get_template('bases_core/about.html')
    c = RequestContext(request, {'active_tab': 'about'})
    return HttpResponse(t.render(c))

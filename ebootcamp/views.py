from django.template import RequestContext, loader
from django.http import HttpResponse

def about(request):
    t = loader.get_template('ebootcamp/about.html')
    c = RequestContext(request, {'active_tab' : 'programs'})
    return HttpResponse(t.render(c))

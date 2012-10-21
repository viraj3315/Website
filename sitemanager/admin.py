import sys
from django.contrib import admin
from sitemanager.models import Page
from sitemanager.forms import PageAdminForm

class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm
    
    #def get_form(self, request, obj=None, **kwargs):
        #form = super(PageAdmin, self).get_form(request, obj, **kwargs)
        #form = PageAdminForm
        #print >>sys.stderr, form.is_valid()
        #for group in request.user.groups.all():
        #    print >>sys.stderr, group
        #return form

admin.site.register(Page, PageAdmin)

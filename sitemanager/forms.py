import sys
import django.forms as forms
from sitemanager.models import Page

class PageAdminForm(forms.ModelForm):
    #title = forms.CharField(max_length=100, initial='hello world')
    head = forms.CharField(widget=forms.Textarea(attrs={'cols':86,'rows':10}), required=False)
    
    landing = forms.BooleanField(required=False, help_text="Is this the home page for your team?")
    #print >>sys.stderr, model.groups
    class Meta:
        model = Page
        #exclude = ('groups',)

    

from django.db import models
from django.contrib.auth.models import Group

class Page(models.Model):
    groups = models.ManyToManyField(Group)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100, default='')
    head = models.TextField(default='')
    body = models.TextField(default='') 
    landing = models.BooleanField()
    landing.short_description = "Is this the home page?"

    def __unicode__(self):
        return self.title

class Landing_Page(models.Model):
    page = models.OneToOneField(Page)

    # make the landing page behave like a singleton

    def save(self):
        self.id=1
        super(Landing_Page, self).save()

    def delete(self):
        pass

    def __unicode__(self):
        return self.page.title

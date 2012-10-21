from django.db import models
from django.contrib.auth.models import Group

class Page(models.Model):
    groups = models.ManyToManyField(Group)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100, default='')
    head = models.TextField(default='')
    body = models.TextField(default='') 

    def __unicode__(self):
        return self.title

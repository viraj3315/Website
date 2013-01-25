from django.db import models

# Create your models here.
class Event(models.Model):
    PROGRAM_CHOICES = (
        ('OT', 'Other'),
        ('15', 'BASES 150k Challenge'),
        ('EB', 'Entrepreneurship Bootcamp'),
        ('ET', 'ETL'),
        ('CF', 'Startup Career Fair'),
        ('LI', 'Links'),
        ('IN', 'Internal'),
    )
    title = models.CharField(max_length=200)
    program = models.CharField(max_length=2,
                               choices=PROGRAM_CHOICES,
                               default='OT')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    url = models.CharField(max_length=50)
    image = models.ImageField()
    blurb = models.TextField()
    content = models.TextField()


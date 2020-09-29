from django.db import models


# Create your models here.
from django.template.defaultfilters import slugify

from job import settings


class Job(models.Model):
    title = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    CHOICES = (
        ('full_time','full time'),
        ('part_time','part time'),
        ('freelance','freelance'),
        ('internship','internship'),
        ('temporary','temporary'),
    )
    job_type = models.CharField(max_length=100,blank=False,default=None,choices=CHOICES)
    location = models.CharField(max_length=200,blank=False,default=None)
    description = models.TextField(blank=False,default=None)
    publishing_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default=None,editable=False)
    employer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=None)


    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args,**kwargs)
    class Meta:
        ordering = ('-id',)




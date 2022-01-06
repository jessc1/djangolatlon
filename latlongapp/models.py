from django.contrib.gis.db import models
from django.contrib.gis import forms
from django.urls import reverse

class Local(models.Model):
    
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    lon = models.FloatField()
    lat = models.FloatField()
    area = models.FloatField()
    region = models.CharField(max_length=100)     
    visited = models.DateTimeField(null=True)
                    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):        
        return reverse('local_detail',args=[str(self.id)])
    

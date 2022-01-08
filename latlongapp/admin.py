from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import Local

@admin.register(Local)
class LocalAdmin(OSMGeoAdmin):
    list_display = ('name', 'region')
    

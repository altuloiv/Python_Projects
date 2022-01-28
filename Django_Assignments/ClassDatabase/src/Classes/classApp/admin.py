from django.contrib import admin

##impotyinh my djangoclasses from models file
from .models import djangoClasses
##register my objects 
admin.site.register(djangoClasses)

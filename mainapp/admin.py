from django.contrib import admin
from .models import *
# Register your models here.
 
class allpost(admin.ModelAdmin):
    list_display=["__str__",'author', 'content','image']
    search_fields=['Welcome_text',]
    list_per_page = 10

admin.site.register(Post,allpost) 


class allprofile(admin.ModelAdmin):
    list_display=["__str__",'user','image']
    list_per_page = 10

admin.site.register(Profile,allprofile) 



class bgAdmin(admin.ModelAdmin):
    list_display=["__str__",'title']
    list_per_page = 10

admin.site.register(Background,bgAdmin) 
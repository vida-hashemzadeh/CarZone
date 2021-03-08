from django.contrib import admin
from .models import Team
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
    def Imageteam (self,object):
        return format_html('<img src="{}" width="50" style="border-radius: 50%;" />'.format(object.photo.url))

    Imageteam.short_description = "Image"

    list_display = ('id','Imageteam','first_name','last_name','designation')
    list_display_links = ('id','Imageteam','first_name',)
    search_fields = ('first_name' , 'last_name')
    list_filter = ('first_name','last_name','designation')
# Register your models here.
admin.site.register (Team,TeamAdmin)

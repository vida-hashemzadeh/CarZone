from django.contrib import admin
from .models import Car
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):
    def Imagecar (self,object):
        return format_html('<img src="{}" width="50" style="border-radius: 50%;" />'.format(object.car_photo))

    Imagecar.short_description = "Image"

    list_display =('id','car_title','Imagecar', 'color', 'model','year','body_style','is_featured')
    list_display_links = ('id','car_title','model')
    list_editable = ('is_featured',)
    search_fields = ('id','car_title','color')
    list_filter = ('city', 'model','body_style',)


# Register your models here.
admin.site.register (Car,CarAdmin)


from django.contrib import admin
from django.utils.html import format_html
from .models import Pic,Material,Color,Classify


admin.site.register(Material)
admin.site.register(Color)
admin.site.register(Classify)


class PicAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))
    def name_tag(self,obj):
        return obj.image.name

    image_tag.short_description = 'Image'
    name_tag.short_description='File Name'
    list_display = ['name_tag','image_tag']


admin.site.register(Pic,PicAdmin)
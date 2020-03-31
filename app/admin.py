
from django.contrib import admin

from .models import Pic,Material,Color,where_to_use

admin.site.register(Pic)
admin.site.register(Material)
admin.site.register(Color)
admin.site.register(where_to_use)
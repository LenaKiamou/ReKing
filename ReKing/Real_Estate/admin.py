from django.contrib import admin
from .models import *

admin.site.register(Features)

class ImagesAdmin(admin.StackedInline):
    model = Images

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    inlines = [ImagesAdmin]

    class Meta:
        model = House

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass

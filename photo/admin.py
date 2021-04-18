from django.contrib import admin
from .models import Photos


class PhotosAdmin(admin.ModelAdmin):
    pass


admin.site.register(Photos, PhotosAdmin)

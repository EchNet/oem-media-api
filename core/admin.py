from admin_auto_filters.filters import AutocompleteFilterFactory
from django.contrib import admin

from . import models


@admin.register(models.MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
  list_display = ("id", "file", "created_at")


@admin.register(models.MediaFileTag)
class MediaFileTagAdmin(admin.ModelAdmin):
  list_display = (
      "media_file",
      "key",
      "value",
  )

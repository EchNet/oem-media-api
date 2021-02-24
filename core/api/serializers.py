from rest_framework import serializers

from core.models import MediaFile


class MediaFileSerializer(serializers.ModelSerializer):
  class Meta:
    model = MediaFile
    fields = ("id", "file", "created_at")

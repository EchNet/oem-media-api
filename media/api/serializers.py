from rest_framework import serializers

from media.models import MediaFile


class MediaFileSerializer(serializers.ModelSerializer):
  class Meta:
    model = MediaFile
    fields = ("id", "file", "created_at")

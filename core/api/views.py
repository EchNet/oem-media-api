import logging

from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, views
from rest_framework.response import Response

from core import models
from core.api import serializers

logger = logging.getLogger(__name__)


class PingView(views.APIView):
  def get(self, request, *args, **kwargs):
    return Response({"ping": "pong"})


class ListCreateMediaFileView(generics.ListCreateAPIView):
  queryset = models.MediaFile.objects.all()
  serializer_class = serializers.MediaFileSerializer

  def get_queryset(self):
    queryset = super().get_queryset().exclude(deleted=True)
    for key, value in self.request.query_params.items():
      queryset = queryset.filter(tags__key=key, tags__value=value)
    return queryset

  def create(self, request):
    # Accept either the image file or the image file name.
    file_data = request.FILES.get("file", None)
    file_name = request.data.get("file", None)
    if file_data:
      file = file_data
    elif file_name:
      file = file_name
    else:
      raise ValidationError("missing file")

    tags = request.data.get("tags", "").split(",")
    if not tags[0]:
      raise ValidationError("missing tags")

    media_file = models.MediaFile.objects.create(file=file)
    for t in tags:
      key = t.split("=")[0]
      value = t[(len(key) + 1):]
      models.MediaFileTag.objects.create(media_file=media_file, key=key, value=value)
    return Response(serializers.MediaFileSerializer(media_file).data, status.HTTP_201_CREATED)

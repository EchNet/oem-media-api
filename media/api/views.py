import logging

from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import generics, parsers, status, views
from rest_framework.response import Response

from media import models
from . import serializers

logger = logging.getLogger(__name__)


class PingView(views.APIView):
  def get(self, request, *args, **kwargs):
    return Response({"ping": "pong"})


class ListCreateMediaFileView(generics.ListCreateAPIView):
  queryset = models.MediaFile.objects.all()
  serializer_class = serializers.MediaFileSerializer
  parser_classes = (parsers.MultiPartParser, )

  def get_queryset(self):
    queryset = super().get_queryset().exclude(deleted=True)
    for key, value in self.request.query_params.items():
      if key.isalnum() and value and value.isalnum():
        queryset = queryset.filter(tags__key=key, tags__value=value)
    return queryset

  def create(self, request):
    serializer = serializers.MediaFileSerializer(data=request.data)
    if not serializer.is_valid():
      return JsonResponse(serializer.errors, status=400)
    media_file = serializer.save()
    for key, value in self.request.POST.items():
      if not key in ("file", "submit"):
        models.MediaFileTag.objects.create(media_file=media_file, key=key, value=value.lower())
    return Response(serializer.data, status.HTTP_201_CREATED)

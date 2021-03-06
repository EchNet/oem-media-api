import logging

from rest_framework import generics, status, views
from rest_framework.response import Response

from content import models
from content.api import serializers

logger = logging.getLogger(__name__)


class ListCreateContentSectionView(generics.ListCreateAPIView):
  queryset = models.ContentSection.objects.all().order_by("id")
  serializer_class = serializers.ContentSectionSerializer


class ListCreateContentVariantView(generics.ListCreateAPIView):
  queryset = models.ContentVariant.objects.exclude(deleted=True).order_by("id")

  def get_serializer_class(self, *args, **kwargs):
    if self.request.method == "GET":
      return serializers.ListContentVariantSerializer
    else:
      return serializers.ContentVariantSerializer


class RetrieveUpdateContentVariantView(generics.RetrieveUpdateAPIView):
  queryset = models.ContentVariant.objects.exclude(deleted=True)
  serializer_class = serializers.ContentVariantSerializer

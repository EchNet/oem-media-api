from rest_framework import serializers

from content.models import ContentSection, ContentVariant


class ContentSectionSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContentSection
    fields = ("id", "name")


class ContentVariantSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContentVariant
    fields = ("id", "section", "text")


class ListContentVariantSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContentVariant
    fields = ("id", "section")

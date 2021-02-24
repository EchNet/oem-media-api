import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

SHORT_MAX_LENGTH = 16
MEDIUM_MAX_LENGTH = 40
LONG_MAX_LENGTH = 100


class MediaFile(models.Model):
  """
    A pointer to an image or other type of media file in storage.
  """

  # Path to the file in storage.
  file = models.FileField(blank=False, null=False, verbose_name=_("file"))

  # When this record was created.
  created_at = models.DateTimeField(
      auto_now_add=True,
      editable=False,
      verbose_name=_("created at"),
  )

  def __str__(self):
    return str(self.file)


class MediaFileTag(models.Model):
  """
    Metadata key-value pair associated with a media file.
  """

  # The associated media file.
  media_file = models.ForeignKey(
      blank=False,
      db_index=True,
      null=False,
      on_delete=models.CASCADE,
      related_name="tags",
      to=MediaFile,
      verbose_name=_("media file"),
  )

  # The key.
  key = models.CharField(
      blank=False,
      null=False,
      max_length=MEDIUM_MAX_LENGTH,
      verbose_name=_("tag key"),
  )

  # The value.
  value = models.TextField(
      blank=False,
      null=True,
      verbose_name=_("tag value"),
  )

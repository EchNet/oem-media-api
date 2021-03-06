from django.db import models
from django.utils.translation import ugettext_lazy as _


class ContentConfiguration(models.Model):
  """
    Key-value storage for content configurations. 
  """

  # In practice, the key is a serialized website-year-make-model tuple.
  key = models.TextField(
      blank=False,
      db_index=True,
      null=False,
      unique=True,
      verbose_name=_("website"),
  )

  # Unstructured value.
  config = models.JSONField()


class ContentSection(models.Model):
  """ A logical section of the output document.  Its contents may vary. """

  # The name of the content section.
  name = models.CharField(
      blank=False,
      db_index=True,
      null=False,
      max_length=16,
      unique=True,
      verbose_name=_("section id"),
  )


class ContentVariant(models.Model):
  """
    There may be many variants for a single section.
  """

  # The section that this text is intended for.
  section = models.ForeignKey(
      blank=False,
      db_index=True,
      null=False,
      on_delete=models.CASCADE,
      related_name="variants",
      to=ContentSection,
      verbose_name=_("section"),
  )

  # The HTML text.
  text = models.TextField(
      blank=False,
      null=False,
      verbose_name=_("text"),
  )

  # For soft deletion.
  deleted = models.BooleanField(
      blank=True,
      default=False,
      null=True,
      verbose_name=("deleted"),
  )

import logging
import requests

from bs4 import BeautifulSoup
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.views.generic import View

from . import models

logger = logging.getLogger(__name__)


class MediaRedirectView(View):
  def get(self, request, *args, **kwargs):
    slug = kwargs.get("slug")
    _v, year, make, model = slug.split("-")
    q = models.MediaFile.objects.exclude(deleted=True)
    for key, value in (("year", year), ("make", make), ("model", model)):
      q = q.filter(tags__key=key, tags__value=value)
    media_file = q.first()
    if not media_file:
      raise Http404()
    return redirect(str(media_file.file))

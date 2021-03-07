import logging
import requests

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View

from . import models

logger = logging.getLogger(__name__)


class PreviewView(View):
  def get(self, request, *args, **kwargs):
    website = request.GET.get("website")
    slug = request.GET.get("slug")
    url = f"https://www.{website}/v-{slug}"
    response = requests.get(url)
    return HttpResponse(response.text)

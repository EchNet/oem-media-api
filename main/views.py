import logging

from datetime import timedelta
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)


class PageView(TemplateView):
  def get(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return redirect("login")
    return super().get(request, *args, **kwargs)


class HomeView(PageView):
  template_name = "home.html"

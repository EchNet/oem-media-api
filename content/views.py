import logging
import requests

from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import Template, Context
from django.views.generic import View

from . import models

logger = logging.getLogger(__name__)


class ProxyManager:
  proxy = "http://spa7cc30b3:Gnu8s-word@gate.dc.smartproxy.com:20000"
  proxies = {
      "http": proxy,
      "https": proxy,
  } if proxy else None


class PageBuilder:
  def __init__(self, website, slug, ccfg):
    self.website = website
    self.slug = slug
    self.ccfg = ccfg

  def build(self):
    url = f"https://www.{self.website}/v-{self.slug}"
    logger.info(f"Request {url}")
    resp = requests.get(url, timeout=5, proxies=ProxyManager.proxies)
    text = resp.text
    soup = BeautifulSoup(text, "html.parser")

    slots = {}
    for slot_name in ("meta", "header", "body", "footer"):
      slots[slot_name] = self.create_slot(soup, slot_name)

    for section in self.ccfg.config["sections"]:
      cs = models.ContentSection.objects.get(id=section["sid"])
      section_text = self.expand_template(section["vid"])
      logger.info(section_text)
      section_soup = BeautifulSoup(section_text, "html.parser")
      slots[cs.slot].append(section_soup)

    return str(soup)

  def create_slot(self, soup, slot_name):
    if slot_name == "header":
      container = soup.find("div", class_="left-content")
      h1 = container.find("h1")
      h1.extract()
      h3 = container.find("h3")
      h3.extract()
    elif slot_name == "footer":
      container = soup.select("footer")[0]
    elif slot_name == "body":
      picker = soup.find("div", class_="oem-vehicle-picker-module")
      container = picker.parent.parent
      picker.extract()
    elif slot_name == "meta":
      container = soup.select("head")[0]
    return container

  def expand_template(self, variant_id):
    cv = models.ContentVariant.objects.get(id=variant_id)
    template = Template(cv.text)
    year, make, model = self.slug.split("-")
    make = make.capitalize()
    model = model.capitalize()
    website = self.website
    context = Context({
        "year": year,
        "make": make,
        "model": model,
        "website": website,
    })
    return template.render(context)


class PreviewView(View):
  def get(self, request, *args, **kwargs):
    website = request.GET.get("website")
    slug = request.GET.get("slug")
    ccfg = get_object_or_404(models.ContentConfiguration.objects.all(), key=f"{website}-{slug}")
    text = PageBuilder(website, slug, ccfg).build()
    return HttpResponse(text)

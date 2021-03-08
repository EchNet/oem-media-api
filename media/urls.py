from django.conf.urls import url

from . import views

urlpatterns = [
    url('^(?P<slug>[a-zA-Z0-9-.,]+)$', views.MediaRedirectView.as_view()),
]

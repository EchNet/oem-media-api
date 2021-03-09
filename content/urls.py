from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^preview$', views.PreviewView.as_view()),
    url(r'^raw$', views.RawView.as_view()),
]

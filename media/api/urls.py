from django.conf.urls import url

from . import views as api_views

urlpatterns = [
    url(r'^ping$', api_views.PingView.as_view()),
    url(r'^media$', api_views.ListCreateMediaFileView.as_view()),
]

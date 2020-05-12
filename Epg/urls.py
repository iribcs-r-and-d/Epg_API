from django.conf.urls import url
from spyne.server.django import DjangoView
from Aban.views import Epg_service, app

urlpatterns = [
    url(r'^data/', Epg_service),
    url(r'^api/', DjangoView.as_view(application=app)),
]

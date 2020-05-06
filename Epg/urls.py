from django.conf.urls import url, include
from django.contrib import admin
from Aban.views import *
from Aban import views
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoView

urlpatterns = [
    url('/Data/', NoteAPIView.as_view(services={NoteAPIView}, in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())),
]
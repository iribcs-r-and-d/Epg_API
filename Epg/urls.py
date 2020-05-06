from django.conf.urls import url, include
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoView
from Aban.models import NoteAPIView

urlpatterns = [
    url('/Data/', NoteAPIView.as_view(services={NoteAPIView}, in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())),
]
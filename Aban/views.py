from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import NoteSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase
from spyne.error import ResourceNotFoundError, ResourceAlreadyExistsError
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable
from spyne.util.django import *
from Aban.models import Note

class NoteAPIView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['channel','program']
    queryset = Note.objects.all()
    serializer_class = NoteSerializer




app = Application([NoteAPIView],
    'spyne.examples.django',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

Epg_service = csrf_exempt(DjangoApplication(app))


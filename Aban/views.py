from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
from spyne.application import Application
from spyne.decorator import rpc
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.error import ResourceAlreadyExistsError
from spyne.model.primitive import Integer
from spyne.util.django import DjangoComplexModel, Service, ResourceNotFoundError

from Aban.models import Note

class NoteContainer(DjangoComplexModel):
    class Attributes(DjangoComplexModel.Attributes):
        django_model = Note

class NoteContainerService(Service):
    @rpc(Integer, _returns=NoteContainer)
    def get_container(ctx, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise ResourceNotFoundError('Container')

    @rpc(NoteContainer, _returns=NoteContainer)
    def create_container(ctx, container):
        try:
            return Note.objects.create(**container.as_dict())
        except IntegrityError:
            raise ResourceAlreadyExistsError('NoteContainer')



app = Application([NoteContainerService],
    'Epg.Aban',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

Epg_service = csrf_exempt(DjangoApplication(app))

#
# class NoteAPIView(generics.ListCreateAPIView):
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['channel','program']
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#
#
#
#
# app = Application([NoteAPIView],
#     'spyne.examples.django',
#     in_protocol=Soap11(validator='lxml'),
#     out_protocol=Soap11(),
# )
#
# Epg_service = csrf_exempt(DjangoApplication(app))
#

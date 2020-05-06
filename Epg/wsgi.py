import os
from wsme import WSRoot, expose
from django.core.wsgi import get_wsgi_application
from Aban.views import NoteAPIView

class NoteAPIView(WSRoot):
    @expose(unicode, unicode) 
    
ws=NoteAPIView(protocols=['restjson', 'restxml', 'soap'])
application = ws.wsgiapp()
import os
from wsme import WSRoot, expose
from Aban.models import Note

class Note(WSRoot):
    @expose(unicode, unicode) 

ws=NoteAPIView(protocols=['restjson', 'restxml', 'soap'])
application = ws.wsgiapp()
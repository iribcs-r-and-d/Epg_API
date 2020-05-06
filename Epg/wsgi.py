"""
WSGI config for Epg project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from wsme import WSRoot, expose
from django.core.wsgi import get_wsgi_application


class MyService(WSRoot):
    @expose(unicode, unicode)  # First parameter is the return type,
                               # then the function argument types
    def hello(self, who=u'World'):
        return u"Hello {0} !".format(who)

ws = MyService(protocols=['restjson', 'restxml', 'soap'])
application = ws.wsgiapp()

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Epg.settings')

#application = get_wsgi_application()

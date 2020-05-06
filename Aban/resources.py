#from tastypie.resources import ModelResource
#from Aban.models import Note
#from tastypie.authorization import Authorization



#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import (
#    SearchFilter,
#        
#        )
#**********************************
#class NoteResource(ModelResource):
#    class Meta:
        
#**********************        
        
#********************************************        
#        queryset = Note.objects.all()
#        resource_name = 'Epg'
#        authorization = Authorization()
        
#********************************************        
        
#        def get_queryset(self):
#            req = self.request
#            print(req)
#        Model.objects.filter
#        queryset2 = Note.objects.get(id=3)

#        filter_backends = [DjangoFilterBackend]
#        filterset_fields = ['id']

#        filter_fields = ('id',)
#        queryset2 = queryset2.filter(Epg__username=username)
#        fields = ['ch', 'Name', 'visit', 'dur']

#            id = req.query_params.get('id')
#            if id:
#                self.queryset = Note.objects.filter(id=id)
#                return self.queryset
#            else:
#                return self.queryset
#        def get_queryset(self):
#            queryset = Note.objects.all()
#            ch = self.request.query_params.get('ch', None)
#        
#            if ch is not None:
            
#                queryset = queryset.filter(ch=ch)


#return ModelResource.queryset
        
#            return queryset
    
#    def get_queryset(self):
#        req = self.request
#        print(req)
#        id = req.query_params.get('id')
#        if id:
#            self.queryset = Note.objects.filter(id=3)
#            return self.queryset
#        else:
#            return self.queryset

        

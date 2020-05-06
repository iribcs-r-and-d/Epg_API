# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 15:06:11 2019

@author: USER
"""
#from tastypie.resources import ModelResource

from rest_framework import serializers
from Aban.models import Note
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
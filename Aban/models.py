
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import NoteSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
# Create your models here.

 
class Note(models.Model):
    channel = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    duration=models.IntegerField()
    visit=models.IntegerField(max_length=200)
    month=models.CharField(max_length=200)


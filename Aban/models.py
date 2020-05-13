from django.db import models


class Note(models.Model):
    channel = models.CharField()
    program = models.CharField()
    start_date = models.DateTimeField()
    duration = models.IntegerField()
    visit = models.IntegerField()
    month = models.CharField()

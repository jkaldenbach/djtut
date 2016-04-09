import datetime
from django.db import models
from django.utils import timezone

class EventClass(models.Model):
    class Meta:
        abstract = True
        
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    def is_active(self):
        now = timezone.now()
        return self.start_date <= now <=self.end_date

class Initiative(EventClass):
    initiative_name = models.CharField(max_length=200)

    def __str__(self):
        return self.initiative_name

class Program(EventClass):
    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=200)
    budget = models.IntegerField(default=0)

    def __str__(self):
        return self.program_name

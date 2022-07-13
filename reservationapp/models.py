from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nazwa')
    capacity = models.PositiveIntegerField(verbose_name='Pojemność')
    projector_availability = models.BooleanField(default=False, verbose_name='Dostępność rzutnika')

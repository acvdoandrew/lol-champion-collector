from unicodedata import name
from django.db import models

class Champion(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    epithet = models.TextField(max_length=100)
    hours = models.IntegerField()

    def __str__(self):
        return self.name


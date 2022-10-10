from audioop import reverse
from unicodedata import name
from django.db import models
from django.urls import reverse

class Champion(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    epithet = models.TextField(max_length=100)
    hours = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('champions_detail', kwargs={'pk': self.id })


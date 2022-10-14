from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class SkinTheme(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('skins_detail', kwargs={'pk': self.id})


class Champion(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    epithet = models.TextField(max_length=100)
    hours = models.IntegerField()
    skins = models.ManyToManyField(SkinTheme)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('champions_detail', kwargs={'pk': self.id })

class Matches(models.Model):
    RESULTS = (
        ('V', 'VICTORY'),
        ('D', 'DEFEAT'),
    )
    date = models.DateField('match date')
    match = models.CharField(max_length=1, choices=RESULTS, default=RESULTS[0][0])
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_match_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']


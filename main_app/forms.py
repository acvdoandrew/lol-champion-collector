from django.forms import ModelForm
from .models import Matches

class MatchesForm(ModelForm):
    class Meta:
        model = Matches
        fields = ('date', 'match')
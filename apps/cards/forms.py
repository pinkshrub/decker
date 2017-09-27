from django.forms import ModelForm
from models import Card

class CardForm(ModelForm):
    """This form allows Card creation"""
    class Meta:
        model = Card
        fields = ['name','cost']
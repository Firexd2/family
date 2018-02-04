from django import forms
from baby.models import CurrentDay, BabyWeight
from django.forms.widgets import *


class CurrentDayForm(forms.ModelForm):
    class Meta:
        exclude = ['overall_volume', 'date']
        model = CurrentDay
        widgets = {
            'toilet': CheckboxInput
        }


class WeightForm(forms.ModelForm):
    class Meta:
        model = BabyWeight
        exclude = ['']

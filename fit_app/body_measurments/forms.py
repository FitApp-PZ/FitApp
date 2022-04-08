from logging import PlaceHolder
from time import time
from django import forms
from datetime import date, datetime

from body_measurments.models import BodyCircuits, BodyMeasurements, Goals

class DateInput(forms.DateInput):
    input_type = 'date'

class BodyMeasurementsForm(forms.ModelForm):
    class Meta:
        model = BodyMeasurements
        fields = ['weight', 'height','date']
        
    date = forms.DateField(widget=DateInput, initial=date.today(), label="Data")
    weight = forms.FloatField(label='Waga')
    height = forms.FloatField(label='Wzrost')

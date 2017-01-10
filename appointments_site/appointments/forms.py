import datetime

from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.core.exceptions import ValidationError

class AppointmentForm(forms.Form):
	time = forms.TimeField(required=False)
	date = forms.DateField(widget=SelectDateWidget(years=range(datetime.date.today().year, datetime.date.today().year+100)), required=True)
	description = forms.CharField(widget=forms.Textarea, required=False)

class AppointmentSearchForm(forms.Form):
    keyword = forms.CharField(required=False,
                                widget=forms.TextInput(attrs={'id': 'keyword','autocomplete':'off','placeholder': 'Search Appointment'}))
import datetime

from django import forms

class AppointmentForm(forms.Form):
	time = forms.TimeField(required=False)
	date = forms.DateField(widget=SelectDateWidget(years=range(1920, datetime.date.today().year)), required=True)
	description = forms.CharField(widget=forms.Textarea, required=False)

class AppointmentSearchForm(forms.Form):
    keyword = forms.CharField(required=False,
                                widget=forms.TextInput(attrs={'id': 'keyword','autocomplete':'off','placeholder': 'Search Appointment'}))
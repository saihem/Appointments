from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Appointment(models.Model):
	date = models.DateField(null=True)
	time = models.TimeField(null=True)
	description = models.TextField(null=True)
	created_on = models.DateTimeField(auto_now_add=True, null=True)
	modifed_on = models.DateTimeField(null=True)
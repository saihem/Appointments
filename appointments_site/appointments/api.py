from django.db.models import Q
from appointments.models import Appointment

class AppointmentsInstanceResource(object):
	def _post(self, kwargs):
		date = kwargs.get("date", None)
		time = kwargs.get("time", None)
		description = kwargs.get("description", None)
		appointment = Appointment()
		appointment.date = date
		appointment.time = time
		appointment.description = description
		appointment.save()
		return appointment


class AppointmentsListResource(object):
	def _get(self, date):
		'''
			Gets appointments starting from the current day
		'''
		appointments = Appointment.objects.filter(Q(date__gte=date)).order_by('-created_on')
		return appointments, appointments.count()

	def get_matching_appointments(self, query):
		#query = query_dict['keyword'].strip()
		results = Appointment.objects.filter(Q(date__icontains=query)| Q(time__icontains=query)| Q(description__icontains=query))
		return list(results), results.count()

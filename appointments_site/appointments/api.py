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
		print "DATE", date
		appointments = Appointment.objects.filter(Q(date__gte=date)).order_by('-created_on')
		for app in appointments:
			print app.created_on, "created needs to be less than DATE", date,
			print app.date
			print app.description
		print "END OF APP STUFF" 
		return appointments, appointments.count()
	
	def get_matching_appointments(self, query_dict):
		query = query_dict['keyword'].strip()
		results = Appointment.objects.filter(Q(date__icontains=query)| Q(time__icontains=query)| Q(description__icontains=query))
		print "check results"* 5, results
		return list(results), results.count()
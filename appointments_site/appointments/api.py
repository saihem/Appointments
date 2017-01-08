from appointments.models import Appointment

class AppointmentsInstanceResource(object):
	def _post(self, kwargs):
		date = kwargs.get("date", None)
		time = kwargs.get("time", None)
		description = kwargs.get("description", None)
		#appointment = Appointment(date=date, time=time, description=description)
		appointment = Appointment()
		appointment.date = date
		appointment.time = time
		appointment.description = description
		appointment.save()
		return appointment
	def _get(self, date):
		if date:
			return Appointment.objects.get(date=date)
		return Appointment.objects.all()

class AppointmentsListResource(object):
	def _get(self, kwargs):

	def get_matching_appointments(self, query):
		query = query.strip()
		results = Appointment.objects.filter(Q(date__icontains=query)| Q(time__icontains=query)| Q(description__icontains=query))
		return list(results)
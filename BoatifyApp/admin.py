from django.contrib import admin
from .models import Contact, Schedule
from payment.models import Seatres, booking, Ticket
# Register your models here.

admin.site.register(Contact)
admin.site.register(Schedule)
admin.site.register(Seatres)
admin.site.register(booking)
admin.site.register(Ticket)
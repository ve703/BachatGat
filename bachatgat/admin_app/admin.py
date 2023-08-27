from django.contrib import admin
from .models import MeetingEvent
from .models import Attendance


# Register your models here.
from .models import profile

admin.site.register(profile)
admin.site.register(MeetingEvent)
admin.site.register(Attendance)


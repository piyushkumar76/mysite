from django.contrib import admin

from .models import User_Request, Stations, PoliceEntry

admin.site.register(User_Request)
admin.site.register(Stations)
#admin.site.register(Policemen)
admin.site.register(PoliceEntry)

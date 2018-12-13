from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
Models = (Token,Superadmin,Subadmin,Borrower,Facility,Equipment,Reservation,BorrowerLogs,Logs)

admin.site.register(Models)


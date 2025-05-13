from django.contrib import admin
from .models import Contact, SystemUser

# Register your models here.
admin.site.register(Contact)
admin.site.register(SystemUser)
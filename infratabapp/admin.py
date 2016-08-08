from django.contrib import admin
from infratabapp.models import ReminderDetails, EmailNotification, SMSNotification

# Register your models here.
admin.site.register(ReminderDetails)
admin.site.register(EmailNotification)
admin.site.register(SMSNotification)

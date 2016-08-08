from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.cache import SimpleCache
from tastypie import fields
from infratabapp.models import ReminderDetails, SMSNotification, EmailNotification

class ReminderDetailsResource(ModelResource):

    class Meta:
        queryset = ReminderDetails.objects.all()
        resource_name = "reminder"
        authorization = Authorization()
        always_return_data = True
        cache = SimpleCache(timeout=10)

class EmailNotificationResource(ModelResource):
    reminder = fields.ForeignKey(ReminderDetailsResource, 'reminder')

    class Meta:
        queryset = EmailNotification.objects.all()
        resource_name = "emailnotf"
        excludes = ['id']
        authorization = Authorization()
        always_return_data = True
        cache = SimpleCache(timeout=10)

    def dehydrate(self, bundle):
        bundle.data['reminder'] = bundle.obj.reminder.message
        return bundle

class SMSNotificationResource(ModelResource):
    reminder = fields.ForeignKey(ReminderDetailsResource, 'reminder')

    class Meta:
        queryset = SMSNotification.objects.all()
        resource_name = "smsnotf"
        excludes = ['id']
        authorization = Authorization()
        always_return_data = True
        cache = SimpleCache(timeout=10)

    def dehydrate(self, bundle):
        bundle.data['reminder'] = bundle.obj.reminder.message
        return bundle

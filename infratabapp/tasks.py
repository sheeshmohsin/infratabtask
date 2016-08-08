from __future__ import absolute_import

from infratabtask.celery import app
from infratabapp.models import ReminderDetails
from celery import Task
from infratabapp.utils import send_email_notf, send_phone_notf


class SendNotf(Task):

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk', None)

    def run(self):
        self.get_object()
        self.email_notf()
        self.phone_notf()

    def get_object(self):
        self.obj = ReminderDetails.objects.get(pk=self.pk)
        self.message = self.obj.message

    def email_notf(self):
        self.email_list = []
        for x in self.obj.emailnotification_set.all():
            self.email_list.append(x.email)
        send_email_notf(self.email_list, self.message)

    def phone_notf(self):
        self.phone_list = []
        for y in self.obj.smsnotification_set.all():
            self.phone_list.append(y.phone)
        send_phone_notf(self.phone_notf, self.message)

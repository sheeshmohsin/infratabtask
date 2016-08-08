from django.db import models

# Create your models here.
class ReminderDetails(models.Model):
    datetime = models.DateTimeField(null=False, blank=False)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.message

class EmailNotification(models.Model):
    reminder = models.ForeignKey(ReminderDetails)
    email = models.EmailField(blank=False, null=False)

    class Meta:
        unique_together = (("reminder", "email"),)

    def __str__(self):
        return self.email

class SMSNotification(models.Model):
    reminder = models.ForeignKey(ReminderDetails)
    mobile = models.CharField(max_length=15)

    class Meta:
        unique_together = (("reminder", "mobile"),)

    def __str__(self):
        return self.mobile

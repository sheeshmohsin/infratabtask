from django.db.models.signals import post_save
from django.dispatch import receiver
from infratabapp.tasks import SendNotf


def update_message(sender, instance, **kwargs):
    task = SendNotf()
    task.apply_async(args=[instance.pk], eta=instance.datetime)
    print("Task queued")

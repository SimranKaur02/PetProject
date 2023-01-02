from django.db.models.signals import *
from .models import Student
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
        print("Student Profile Created!")

#post_save.connect(create_profile,sender = User)

@receiver(post_save, sender = User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.student.save()
        print("Student Profile Updated!")


#post_save.connect(update_profile, sender=User)
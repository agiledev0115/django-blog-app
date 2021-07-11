from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# define a function which creates the profile for new user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# define a function which saves the profile for new user
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
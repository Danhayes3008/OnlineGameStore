from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    name = models.CharField(max_length=250, blank=True)
    birthday = models.DateField(auto_now=False, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_or_update_user_profile (sender, instance, created, **kwargs):
        if created:
            Profile.objects.get_or_create(user=instance)
            instance.profile.save()

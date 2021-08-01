from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Professional
from django.forms import ValidationError
  
  
@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Professional.objects.create(user=instance)
   
@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs):
        instance.professional.save()

# @receiver(pre_save, sender=User)
# def check_email(sender, instance, **kwargs):
#     email = instance.email
#     if sender.objects.filter(email=email).exists():
#         raise ValidationError('Email already exists')

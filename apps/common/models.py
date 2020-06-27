

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=15,unique=True,null=True)
    birth_date = models.DateField(null=True,blank=True)
    bio = models.TextField(max_length=500,blank=True)
    profile_image = models.ImageField(default='default.jpg',upload_to='users/')
    objects = models.Manager
    
    def __str__(self):
        return '%s ' % (self.phone)

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()

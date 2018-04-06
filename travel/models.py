from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    choice = (('0', 'Female'), ('1', 'Male'), ('2', 'Other'))
    college = models.CharField(max_length=100)
    choice1 = (('Gurgaon','Gurgaon'),(),())
    location = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    gender = models.CharField(max_length=6, choices=choice)
    contact = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.user.username
from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    choice = (('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other'))
    college = models.CharField(max_length=100)
    choice1 = (('Gurgaon','Gurgaon'),('Kapriwas','Kapriwas'),('Manesar','Manesar'))
    location = models.CharField(max_length=20, choices=choice1)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    gender = models.CharField(max_length=6, choices=choice)
    contact = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=30)
    aadhar_no = models.CharField(max_length=12,unique=True)

    def __unicode__(self):
        return self.user.username

class Vendors(models.Model):
    username= models.CharField(max_length=10, unique=True, blank=False)
    email = models.EmailField(max_length=30,blank=True)
    choice = (('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other'))
    picture = models.ImageField(upload_to='vendor_images', blank=True)
    gender = models.CharField(max_length=6, choices=choice)
    contact = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=30)
    aadhar_no = models.BigIntegerField(unique=True)
    types=(('Local Transport','Local Transport'),('Teacher','Teacher'),('Car Pool','Car Pool'),('Taxi','Taxi'),
           ('Logistics','Logistics'),('School Bus','School Bus'))
    type=models.CharField(max_length=20,choices=types)

    def __unicode__(self):
        return self.username

class Vendor_services(models.Model):
    username = models.CharField(max_length=10, blank=False)
    date = models.CharField(max_length=15, blank=False)
    time = models.CharField(max_length=10, blank=False)
    price = models.IntegerField()
    seats_count = models.IntegerField()
    vehicle_no = models.CharField(max_length=20)
    transport_mode = models.CharField(max_length=20)
    hop_bml = models.BooleanField(default=False)
    hop_manesar = models.BooleanField(default=False)
    hop_rajiv_chowk = models.BooleanField(default=False)
    hop_iffco_chowk = models.BooleanField(default=False)

    def __unicode__(self):
        return self.username

class user_services(models.Model):
    username = models.CharField(max_length=10, blank=False)
    date = models.CharField(max_length=15, blank=False)
    time = models.CharField(max_length=10, blank=False)
    seats_need = models.IntegerField()
    source_choice = (('BML','BML'),('Manesar','Manesar'),('Rajiv Chowk','Rajiv Chowk'),('Iffco Chowk','Iffco Chowk'))
    source = models.CharField(max_length=15, choices=source_choice)
    destination = models.CharField(max_length=15, choices=source_choice)
    price = models.IntegerField()
    seats_count = models.IntegerField()
    vehicle_no = models.CharField(max_length=20)
    transport_mode = models.CharField(max_length=20)
    vendor_username = models.CharField(max_length=10, blank=False)

    def __unicode__(self):
        return self.username

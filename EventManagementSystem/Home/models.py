from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Discuss if you wanna put image in model also


class Event(models.Model):
    user = models.ForeignKey(User , on_delete = models.SET_NULL, null=True , blank=True, related_name="participated_events")
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    event_date = models.DateField()
    event_location = models.CharField(max_length=800 , default= 'defualt Location')
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True , related_name='created_events')

    class Meta:
        db_table = "Event"


class CustomUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length= 255)
    email = models.EmailField(max_length= 255)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)  # Add last_login field
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = "user"


class Registration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Registration"
        unique_together = ('user', 'event')  # Ensure each user can only register once per event
        


from django.db import models

from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class Room(models.Model):
    ROOM_TYPES=[
        ('Single','Single'),
        ('Double','Double'),
        ('Studio','Studio'),
        ('shared','shared'),
    ]

    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    room_type=models.CharField(max_length=100,choices=ROOM_TYPES)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    location=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    is_available=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='rooms/',blank=True,null=True)
    contact_details=models.CharField(max_length=300,null=True)
    feature=models.TextField(blank=True,null=True)
    advantages=models.TextField(blank=True,null=True)
    contact_name=models.CharField(blank=True,null=True,max_length=100)
    contact_number=models.CharField(blank=True,null=True,max_length=20)


    def __str__(self):
        return self.title
    
class Customer(AbstractUser):
    userType=[('provider','provider'),('finder','finder')]
    user_type=models.CharField(max_length=100,choices=userType,default='customer')
    phoneNumber=models.CharField(max_length=20,blank=False,null=False)
    
    def __str__(self):
        return self.username


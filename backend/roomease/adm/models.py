from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    ROOM_TYPES=[
        ('Single','Single'),
        ('Double','Double'),
        ('Studio','Studio'),
        ('shared','shared'),
    ]

    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    room_type=models.CharField(max_length=100,choices=ROOM_TYPES)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    location=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    is_available=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='rooms/',blank=True,null=True)

    def __str__(self):
        return self.title



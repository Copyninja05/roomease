from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from .models import Room
from .serializers import RoomSerializer
from rest_framework import generics

class RoomViewSet(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer 
class roomDetailView(generics.RetrieveAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer

class roomCreateView(generics.CreateAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
    permission_classes=[IsAuthenticated]

class roomUpdateView(generics.UpdateAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
    permission_classes=[IsAuthenticated]

class roomDeleteView(generics.DestroyAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
    permission_classes=[IsAuthenticated]
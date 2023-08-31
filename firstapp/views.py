from django.shortcuts import render
from .models import Room
from rest_framework import generics
from .serializers import RoomSerializers

# Create your views here.

class RoomView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


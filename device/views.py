from django.shortcuts import render
from rest_framework import generics ,status 
from .models import *
from .serilaizers import *
# Create your views here.
class listview(generics.ListCreateAPIView):
    queryset = devicedetails.objects.all()
    serializer_class = listserializer

class addname(generics.ListCreateAPIView):
    queryset = devicedetails.objects.all()
    serializer_class = listserializer

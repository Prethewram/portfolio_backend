from django.shortcuts import render
from rest_framework import generics ,status 
from .models import *
from .serilaizers import *
from rest_framework.pagination import PageNumberPagination
# Create your views here.
class listview(generics.ListCreateAPIView):
    queryset = devicedetails.objects.all()
    serializer_class = listserializer
    pagination_class = PageNumberPagination

class addname(generics.ListCreateAPIView):
    queryset = devicedetails.objects.all()
    serializer_class = listserializer
    pagination_class = PageNumberPagination

class DeviceDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = devicedetails.objects.all()
    serializer_class = listserializer
    lookup_field = "id"
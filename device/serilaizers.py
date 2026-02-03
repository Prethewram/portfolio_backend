from rest_framework import serializers
from .models import *


class listserializer(serializers.ModelSerializer):
    class Meta:
        model = devicedetails
        fields = '__all__'
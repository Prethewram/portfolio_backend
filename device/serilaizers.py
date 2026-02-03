from rest_framework import serializers
from django.utils.timezone import localtime
from .models import devicedetails


class listserializer(serializers.ModelSerializer):

    class Meta:
        model = devicedetails
        fields = "__all__"



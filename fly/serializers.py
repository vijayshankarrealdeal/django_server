from django.db.models import fields
from rest_framework import  serializers
from  . models import *


class FlightBoardSerializers(serializers.ModelSerializer):
    class Meta:
        model = FlightBoard
        fields = '__all__'
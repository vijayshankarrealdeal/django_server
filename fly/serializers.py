from django.db.models import fields
from rest_framework import  serializers
from  . models import *
from django.contrib.auth.models import  User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']





class FlightBoardSerializers(serializers.ModelSerializer):
    class Meta:
        model = FlightBoard
        fields = '__all__'
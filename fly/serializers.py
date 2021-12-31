from django.db.models import fields
from rest_framework import  serializers
from rest_framework_simplejwt.tokens import RefreshToken
from  . models import *
from django.contrib.auth.models import  User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

class UserSerializerWithToken(UserSerializer):
    access = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','access']
    
    def get_access(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)






class FlightBoardSerializers(serializers.ModelSerializer):
    class Meta:
        model = FlightBoard
        fields = '__all__'
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


class GetBookingDetailsOfUser(serializers.ModelSerializer):
    class Meta:
        model = BookFlightTickets
        fields = ['flight']
        depth = 1


class ShopNationalSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShopsNational
        fields = '__all__'

class ShopInterNationalSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShopsInterNational
        fields = '__all__'

class PreFoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = PreFood
        fields = '__all__'

class PostFoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostFood
        fields = '__all__'


class FlightBoardSerializers(serializers.ModelSerializer):
    class Meta:
        model = FlightBoard
        fields = '__all__'
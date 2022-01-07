from django.db.models import fields
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from . models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCoins
        fields = '__all__'



class UserSerializerWithToken(UserSerializer):
    access = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'access']

    def get_access(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class GetBookingDetailsOfUser(serializers.ModelSerializer):
    class Meta:
        model = BookFlightTickets
        fields = ['id',
                  'flight_image', 'fight_name', 'flight_no',
                  'origin_time',
                  'origin_place',
                  'destination_time',
                  'destination_place', 'duration_stop',
                  'no_stops', 'price', 'refund', 'total_pay', 'cancel', 'checklistcreated'
                  ]


class ChecklistSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChecklistModel
        fields = ['id','Documents', 'Financial', 'Clothes', 'Travelaids',
                  'Appliances', 'Health', 'Toiletries', 'genral_activity']


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


class DealOfferSerializers(serializers.ModelSerializer):
    class Meta:
        model = DealsAndOffers
        fields = '__all__'

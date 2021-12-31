from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k,v in serializer.items():
            data[k] = v
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["POST"])
def register_user(request):
    data = request.data
    try:
        user = User.objects.create(
            username = data['email'],
            email = data['email'],
            password = make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user,many=False)
        return Response(serializer.data)
    except Exception as e:
        message = {'detail':'User with this exits' + str(e)} 
        return Response(message,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_userprofile(request):
    user = request.user
    u_serail = UserSerializer(user,many=False)
    return Response(u_serail.data)

@api_view(["GET"])
def get_flight_board(request):
    flight_board = FlightBoard.objects.all()
    f_serail = FlightBoardSerializers(flight_board,many=True)
    return Response({"data":f_serail.data})

@api_view(["GET"])
def get_shop_national(request):
    s_nat = ShopsNational.objects.all()
    f_serail = ShopNationalSerializers(s_nat,many=True)
    return Response({"data":f_serail.data})

@api_view(["GET"])
def get_shop_international(request):
    interShop = ShopsInterNational.objects.all()
    f_serail = ShopInterNationalSerializers(interShop,many=True)
    return Response({"data":f_serail.data})

@api_view(["GET"])
def get_prefood(request):
    s_nat = PreFood.objects.all()
    f_serail = PreFoodSerializers(s_nat,many=True)
    return Response({"data":f_serail.data})

@api_view(["GET"])
def get_postfood(request):
    interShop = PostFood.objects.all()
    f_serail = PostFoodSerializers(interShop,many=True)
    return Response({"data":f_serail.data})


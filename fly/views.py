from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['email'] = self.user.email
        
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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



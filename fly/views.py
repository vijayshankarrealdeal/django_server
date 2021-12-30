from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *


@api_view(["GET"])
def get_flight_board(request):
    flight_board = FlightBoard.objects.all()
    f_serail = FlightBoardSerializers(flight_board,many=True)
    return Response({"data":f_serail.data})



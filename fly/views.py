from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
import requests


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["POST"])
def register_user(request):
    data = request.data
    try:
        user = User.objects.create(
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except Exception as e:
        message = {'detail': 'User with this exits' + str(e)}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_userprofile(request):
    user = request.user
    u_serail = UserSerializer(user, many=False)
    return Response(u_serail.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_usercoin(request):
    user = request.user
    user_data = UserCoins.objects.filter(user = user)
    print(user_data)
    userX = UserCoinSerializer(user_data,many = True)
    return Response(userX.data)

@api_view(["POST","GET"])
@permission_classes([IsAuthenticated])
def update_usercoin(request):
    user = request.user
    user_data = UserCoins.objects.filter(user = user)
    userX = UserCoinSerializer(user_data,many = True)
    coins = userX.data[0]['coins']
    user_data.update(coins=coins+50)
    userX = UserCoinSerializer(user_data,many = True)
    print(userX.data)
    #user_data.update_or_create(coins = 50)
    return Response("done")

@api_view(["POST","GET"])
@permission_classes([IsAuthenticated])
def deleteblr_usercoin(request):
    user = request.user
    user_data = UserCoins.objects.filter(user = user)
    userX = UserCoinSerializer(user_data,many = True)
    coins = userX.data[0]['coins']
    if coins > 0:
        user_data.update(coins=coins-30)
    userX = UserCoinSerializer(user_data,many = True)
    print(userX.data)
    return Response("done")



###


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def get_booking_details(request):
    user = request.user
    print(user)
    interShop = BookFlightTickets.objects.filter(user=user)
    f_serail = GetBookingDetailsOfUser(interShop, many=True)
    return Response({"data": f_serail.data})


@api_view(["PUT", "GET"])
@permission_classes([IsAuthenticated])
def cancel_ticket(request, pk):
    user = request.user
    print(pk)
    ticket = BookFlightTickets.objects.filter(user=user, id=pk)
    ticket.update(cancel=True)
    return Response({"data": "Success"})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def addchecklistto_ticket(request, pk):
    user = request.user
    data = request.data
    ticket = BookFlightTickets.objects.get(user=user, id=pk)
    Documents = data.get('Documents')
    Financial = data.get('Financial')
    Clothes = data.get('Clothes')
    Travelaids = data.get('Travel aids')
    Appliances = data.get('Appliances')
    Health = data.get('Health')
    Toiletries = data.get('Toiletries')
    genral_activity = data.get('General activities')
    checklistmodel = ChecklistModel(
        ticket=ticket,
        Documents=Documents,
        Financial=Financial,
        Clothes=Clothes,
        Travelaids=Travelaids,
        Appliances=Appliances,
        Health=Health,
        Toiletries=Toiletries,
        genral_activity=genral_activity
    )
    try:
        ticket_x = BookFlightTickets.objects.filter(user=user, id=pk)
        ticket_x.update(checklistcreated=True)
        checklistmodel.save()
    except:
        checklist = ChecklistModel.objects.filter(ticket=ticket)
        checklist.update(ticket=ticket, Documents=Documents, Financial=Financial,
                         Clothes=Clothes,
                         Travelaids=Travelaids,
                         Appliances=Appliances,
                         Health=Health,
                         Toiletries=Toiletries,
                         genral_activity=genral_activity)
    checklist = ChecklistModel.objects.all()
    ser = ChecklistSerializers(checklist, many=True)
    return Response({"data": ser.data})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_checklist(request, pk):
    user = request.user
    print(pk)
    ticke = BookFlightTickets.objects.filter(user=user,id = pk)
    checklist = ChecklistModel.objects.filter(ticket = ticke[0])
    ser = ChecklistSerializers(checklist, many=True)
    return Response({"data": ser.data})




@api_view(["GET"])
@permission_classes([IsAuthenticated])
def delete_ticket(request, pk):
    user = request.user
    print(pk)
    ticket = BookFlightTickets.objects.filter(user=user, id=pk)
    ticket.delete()
    return Response({"data": "Success"})


###
@api_view(["GET"])
def get_movies(request):
    api_key = '38f5b3c12b04920fbe5fd093187951af'
    url = 'https://api.themoviedb.org/3/trending/all/day?api_key='+api_key
    data = requests.get(url)
    return Response(data.json())


@api_view(["GET"])
def get_flight_board(request):
    flight_board = FlightBoard.objects.all()
    f_serail = FlightBoardSerializers(flight_board, many=True)
    return Response({"data": f_serail.data})


@api_view(["GET"])
def get_dealsOffer(request):
    flight_board = DealsAndOffers.objects.all()
    f_serail = DealOfferSerializers(flight_board, many=True)
    return Response({"data": f_serail.data})


@api_view(["GET"])
def get_shop_national(request):
    s_nat = ShopsNational.objects.all()
    f_serail = ShopNationalSerializers(s_nat, many=True)
    return Response({"data": f_serail.data})


@api_view(["GET"])
def get_shop_international(request):
    interShop = ShopsInterNational.objects.all()
    f_serail = ShopInterNationalSerializers(interShop, many=True)
    return Response({"data": f_serail.data})


@api_view(["GET"])
def get_prefood(request):
    s_nat = PreFood.objects.all()
    f_serail = PreFoodSerializers(s_nat, many=True)
    return Response({"data": f_serail.data})


@api_view(["GET"])
def get_postfood(request):
    interShop = PostFood.objects.all()
    f_serail = PostFoodSerializers(interShop, many=True)
    return Response({"data": f_serail.data})


@api_view(["Post"])
def book_flight_ticket(request):
    data = request.data
    email = data.get('email')
    cn = data.get('cardNumber')
    cmon = data.get('cardMonth')
    cyr = data.get('cardYear')
    ctype = data.get('cardType')
    cccv = data.get('cardCvv')
    flightImage = data.get('flight_image')
    fightName = data.get('fight_name')
    flightNo = data.get('flight_no')
    originTime = data.get('origin_time')
    originPlace = data.get('origin_place')
    destinationTime = data.get('destination_time')
    destinationPlace = data.get('destination_place')
    durationStop = data.get('duration_stop')
    noStops = data.get('no_stops')
    price = data.get('price')
    refund = data.get('refund')
    total_pay = data.get('total_price')
    user = User.objects.get(username=email)
    b = BookFlightTickets(
        user=user,
        cardNumber=cn,
        cardMonth=cmon,
        cardYear=cyr,
        cardType=ctype,
        cardCvv=cccv,
        flight_image=flightImage,
        fight_name=fightName,
        flight_no=flightNo,
        origin_time=originTime,
        origin_place=originPlace,
        destination_time=destinationTime,
        destination_place=destinationPlace,
        duration_stop=durationStop,
        no_stops=noStops,
        price=price,
        refund=refund,
        total_pay=total_pay,
        cancel=False,
        checklistcreated=False
    )
    b.save()
    return Response({"data": 'saved'})

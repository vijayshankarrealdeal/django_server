from django.db import models
from django.contrib.auth.models import  User

class FlightBoard(models.Model):
    departure = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    flight = models.CharField(max_length=100)
    airline = models.CharField(max_length=100)
    info_url = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    is_departure = models.BooleanField()
    

    def __str__(self) -> str:
        return self.departure

class FlightBookData(models.Model):
    flight_image = models.CharField(max_length=70)
    fight_name = models.CharField(max_length=70)
    flight_no = models.CharField(max_length=70)
    origin_time = models.CharField(max_length=70)
    origin_place = models.CharField(max_length=70)
    destination_time = models.CharField(max_length=70)
    destination_place = models.CharField(max_length=70)
    duration_stop = models.CharField(max_length=70)
    no_stops = models.CharField(max_length=70)
    price = models.CharField(max_length=70)
    refund = models.CharField(max_length=70)
    total_pay = models.IntegerField()
    cancel = models.BooleanField(default=False)
    def __str__(self) -> str:
        return str(self.total_pay)

class BookFlightTickets(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    flight = models.OneToOneField(FlightBookData,on_delete=models.CASCADE)
    cardNumber = models.CharField(max_length=30)
    cardMonth= models.CharField(max_length=30)
    cardYear= models.CharField(max_length=30)
    cardType= models.CharField(max_length=30)
    cardCvv= models.CharField(max_length=30)
    def __str__(self) -> str:
        return str(self.user.email)


class DealsAndOffers(models.Model):
    title = models.CharField(max_length=100,null=True)
    discount = models.CharField(max_length=100,null=True)
    content = models.CharField(max_length=100,null=True)


class ShopsNational(models.Model):
    img = models.CharField(max_length=2500)
    title  = models.CharField(max_length=2500)
    content = models.CharField(max_length=2500)
    opening = models.CharField(max_length=2500)
    location = models.CharField(max_length=2500)
    contanct_details = models.CharField(max_length=2500)
    
    def __str__(self) -> str:
        return str(self.title)

class ShopsInterNational(models.Model):
    img = models.CharField(max_length=2500)
    title  = models.CharField(max_length=2500)
    content = models.CharField(max_length=2500)
    opening = models.CharField(max_length=2500)
    location = models.CharField(max_length=2500)
    contanct_details = models.CharField(max_length=2500)
    
    def __str__(self) -> str:
        return str(self.title)


class PreFood(models.Model):
    img = models.CharField(max_length=2500)
    title  = models.CharField(max_length=2500)
    content = models.CharField(max_length=2500)
    opening = models.CharField(max_length=2500)
    location = models.CharField(max_length=2500)
    contanct_details = models.CharField(max_length=2500)
    
    def __str__(self) -> str:
        return str(self.title)

class PostFood(models.Model):
    img = models.CharField(max_length=2500)
    title  = models.CharField(max_length=2500)
    content = models.CharField(max_length=2500)
    opening = models.CharField(max_length=2500)
    location = models.CharField(max_length=2500)
    contanct_details = models.CharField(max_length=2500)
    
    def __str__(self) -> str:
        return str(self.title)
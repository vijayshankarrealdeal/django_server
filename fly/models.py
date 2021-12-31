from django.db import models

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

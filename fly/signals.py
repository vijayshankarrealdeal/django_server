from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from .models import UserCoins

def updateUser(sender,instance,**kwargs):
    user = instance
    if user.email != '':
        user.username = user.email

def createCoinData(sender,instance,**kwargs):
    user = instance 
    if user.email != '':
        coins = UserCoins(user = user)
        coins.save()


pre_save.connect(updateUser,sender = User)
post_save.connect(createCoinData,sender = User)

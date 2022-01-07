from django.urls import path
from .views import *

urlpatterns = [
    path('user/login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/register', register_user, name='signUP'),
    path('user/profile', get_userprofile, name='user_profile'),
    path('flightstauts/', get_flight_board, name='flight_board'),
    path('nationalshop/', get_shop_national, name='nshop'),
    path('internationalshop/', get_shop_international, name='inshop'),
    path('perfood/', get_prefood, name='prefoood'),
    path('postfood/', get_postfood, name='postfood'),
    path('movies/', get_movies, name='movies'),
    path('booktickets/',book_flight_ticket,name="tikets_book"),
    path('mytrips/',get_booking_details,name="tikets_book"),
    path('dealsoffer/',get_dealsOffer,name="deal_offer"),
    path('cancel_ticket/<str:pk>',cancel_ticket,name="cancel_ticket"),
    path('delete_ticket/<str:pk>',delete_ticket,name="delete_ticket"),
    path('checklist_ticket/<str:pk>',addchecklistto_ticket,name="checklist_ticket"),
    path('get_checklist/<str:pk>',get_all_checklist,name="checklist_ticket"),
    path('get_coins/',get_usercoin,name="blr"),
    path('update_coins/',update_usercoin,name="blr_coinupdate"),
    path('delete_coins/',deleteblr_usercoin,name="blr_coindelete"),



    




]

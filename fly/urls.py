from django.urls import path
from .views import *

urlpatterns = [
    path('user/login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/register', register_user, name='signUP'),
    path('user/profile', get_userprofile, name='user_profile'),
    path('flightstauts/', get_flight_board, name='flight_board'),
    path('nationalshop/', get_shop_national, name='nshop'),
    path('internationalshop/', get_shop_international, name='inshop'),


]

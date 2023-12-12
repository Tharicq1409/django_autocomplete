from django.urls import path
from .  import views

urlpatterns = [
    path('',views.application,name = "applynow"),
    path('autocomplete/',views.autocomplete,name = "autocomplete"),
    path('city-autocomplete/',views.city_auto,name = 'city-autocomplete'),
    path('state-autocomplete',views.state_auto,name = 'state-autocomplete'),
]
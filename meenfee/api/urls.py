from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path

from . import views


urlpatterns = [
    path('ongoingbookings', views.OngoingBookingsListAPIView.as_view(),name="CategoriesCreateDestination"),
   	path('cancelbooking', views.CancelAppointment.as_view(),name="CancelAppointment"),

]












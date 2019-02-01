from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path

from . import views


urlpatterns = [
    path('ongoingbookings', views.OngoingBookingsListAPIView.as_view(),name="OngoingBookings"),
   	path('cancelbooking', views.CancelAppointmentAPIView.as_view(),name="CancelAppointment"),
   	path('re-schedule-appointment', views.ReScheduleAppointmentAPIView.as_view(),name="ReScheduleAppointment"),
   	path('service-is-completed', views.CompletedServiceAPIView.as_view(),name="CompletedService"),

]












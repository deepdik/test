from rest_framework.generics import (
	ListAPIView,
	UpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
	RetrieveAPIView,
	ListCreateAPIView,
	RetrieveUpdateDestroyAPIView
	)
from rest_framework.views import APIView
from rest_framework.permissions import (
	IsAuthenticated,
	IsAdminUser,
	AllowAny,
	)

from meenfee.models import *

from .serializers import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from django_filters import rest_framework as filters
import django_filters
from django.db.models import Avg, Max, Min
from django.db.models import Count
from rest_framework_jwt.authentication import  JSONWebTokenAuthentication

class OngoingBookingsListAPIView(APIView):

	'''
	view for ongoing booking in mybooking tab for requeter( for provide think later)
	it can be access by authenticated user

	remaining------------------------------------------

	(appointment date/time, service availed,
	provider picture, hourly rate, avg star rating,
	manage booking button)
	'''

	authentication_classes = [JSONWebTokenAuthentication]	
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		user = request.user
		qs = RowBooking.objects.filter(requester = user,isacceptedbyprovider=True,ispaymentadd=True)
		data = RowBookingListSerializer(qs,many=True).data
		return Response(data, status = HTTP_200_OK)

class CancelAppointment(APIView):
	'''
	view for cancelation by requestor(for provider think later)
	
	'''


	authentication_classes = [JSONWebTokenAuthentication]	
	permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		user = request.user
		rowbooking_id = request.GET.get('rowbooking_id')
		try:
			obj  = RowBooking.objects.get(id =rowbooking_id)
			if obj.requester == user:
				
				qs = CanceledBooking.objects.create(rowbooking_id = obj,
				canceled_by=user)
				
				# TO DO send notification to provider 

				return Response('appointment cancel successfully' ,status = HTTP_200_OK)
			return Response('this is not your appoinment', status = HTTP_400_BAD_REQUEST)
		except:
			return Response('no data appointment for cancel', status = HTTP_400_BAD_REQUEST)

		
















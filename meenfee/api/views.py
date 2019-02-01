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
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_204_NO_CONTENT,HTTP_201_CREATED

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

class CancelAppointmentAPIView(APIView):
	'''
	view for cancelation by requestor(for provider think later)

	cancelation policy is remaining to be consider
	
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
				
				# TO DO send notification to provider by firebase and save in notification model

				return Response({
							'success':True,
							'msg':'appointment cancel successfully'},
							status=HTTP_200_OK)

			return Response({'success':False,
							'msg':'this is not your appoinment'},
							status = HTTP_400_BAD_REQUEST)
		except:
			return Response({'success':False,
						'msg':'There are no appointment are available for cancel'},
						status=HTTP_204_NO_CONTENT)			

class ReScheduleAppointmentAPIView(APIView):
	authentication_classes = [JSONWebTokenAuthentication]	
	permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		user = request.user
		rowbooking_id = request.GET.get('rowbooking_id')
		qs = RowBooking.objects.filter(id = rowbooking_id,isacceptedbyprovider=True,ispaymentadd=True)
		print(qs)
		if qs.exists() and qs.count()== 1:
			obj = qs.first()

			ReScheduledAppointment.objects.create(rowbooking_id=obj,re_scheduled_by=user)
			print('ok')

			# send notification to provider change status from live running booking
			
			return Response({
					'success':True,
					'msg':'appointment re-schedule notification have been send to your service provider for confirmation'},
					status=HTTP_200_OK)

		return Response({'success':False,
					'msg':'There are no appointment are available for re-schedule'},
					status=HTTP_204_NO_CONTENT)


class ReScheduleAppointmentConfirmAPIView(APIView):
	authentication_classes = [JSONWebTokenAuthentication]	
	permission_classes = (IsAuthenticated,)

	'''

	TO DO For Provider

	'''


class CompletedServiceAPIView(APIView):
	'''
	this is for requestor to confirm service is completed when 
	provider send that service iscompleted
	TO DO  for provider
	'''
	authentication_classes = [JSONWebTokenAuthentication]	
	permission_classes = (IsAuthenticated,)

	def post(self, request, format=None):
		user = request.user
		rowbooking_id = request.GET.get('rowbooking_id')
		try:
			obj = RowBooking.objects.get(id = rowbooking_id,isacceptedbyprovider=True,ispaymentadd=True)	
			# case 1(when provider click on button that service is completed)
			if user == obj.service.user:

				CompletedBooking.objects.create(rowbooking_id=obj,confirmed_by_provider=True)
				obj.isbookingcompleted = True
				obj.save()

				# notification send to requester that service as complete
				# from their end and enable mark complete button for requester
				return Response({
							'success':True,
							'msg':'service mark as complete from Your end and a notification have been send to your requester for confirmation'},
							status=HTTP_200_OK)

			# case 2(when user is requester)
			if user == obj.requester and obj.isbookingcompleted == True:
				try:

					obj = CompletedBooking.objects.get(rowbooking_id=obj,confirmed_by_provider=True)
					if obj.confirmed_by_requester == True:
						return Response({
								'success':True,
								'msg':'you already mark this service is completed'},
								status=HTTP_200_OK)
					else:
						obj.confirmed_by_requester = True
						obj.save()

						# give rating and feedback to service(Popup will be generate in frontend)

						return Response({
								'success':True,
								'msg':'service completed and please give rating'},
								status=HTTP_200_OK)

				except:

					return Response({'success':False,
							'msg':'There are no appointment are available'},
							status=HTTP_204_NO_CONTENT)	

			return Response({'success':False,
							'msg':'you cant complete first from your end'},
							status = HTTP_400_BAD_REQUEST)
		except:
			return Response({'success':False,
						'msg':'There are no appointment are available for Complition or You are already confirmed'},
						status=HTTP_204_NO_CONTENT)			


































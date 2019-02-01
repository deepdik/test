from meenfee.models import *

from rest_framework.serializers import (
	ModelSerializer,
	SerializerMethodField,
	HyperlinkedIdentityField


	)


class CategoryListSerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class CityListSerializer(ModelSerializer):
	class Meta:
		model = City
		fields = '__all__'


class SubCategoryListSerializer(ModelSerializer):
	class Meta:
		model = SubCategory
		fields = [
			'id'
			'subcategory'
		]

class RowBookingListSerializer(ModelSerializer):
	class Meta:
		model = RowBooking
		fields = '__all__'


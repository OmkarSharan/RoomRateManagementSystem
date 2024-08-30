from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from roomrates.models import RoomRate, OverriddenRoomRate, Discount, DiscountRoomRate
from roomrates.serializers import (RoomRateSerializer, OverriddenRoomRateSerializer, 
                          DiscountSerializer, DiscountRoomRateSerializer)

class RoomRateListCreateAPIView(generics.ListCreateAPIView):
    queryset = RoomRate.objects.all()
    serializer_class = RoomRateSerializer

class RoomRateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomRate.objects.all()
    serializer_class = RoomRateSerializer

class OverriddenRoomRateListCreateAPIView(generics.ListCreateAPIView):
    queryset = OverriddenRoomRate.objects.all()
    serializer_class = OverriddenRoomRateSerializer

class OverriddenRoomRateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OverriddenRoomRate.objects.all()
    serializer_class = OverriddenRoomRateSerializer

class DiscountListCreateAPIView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class DiscountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class DiscountRoomRateListCreateAPIView(generics.ListCreateAPIView):
    queryset = DiscountRoomRate.objects.all()
    serializer_class = DiscountRoomRateSerializer

class DiscountRoomRateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiscountRoomRate.objects.all()
    serializer_class = DiscountRoomRateSerializer

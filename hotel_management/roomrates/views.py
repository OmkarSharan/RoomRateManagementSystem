from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from roomrates.models import RoomRate, OverriddenRoomRate, Discount, DiscountRoomRate
from roomrates.serializers import RoomRateSerializer, OverriddenRoomRateSerializer, DiscountSerializer, DiscountRoomRateSerializer

# RoomRate Views
class RoomRateListCreateView(generics.ListCreateAPIView):
    queryset = RoomRate.objects.all()
    serializer_class = RoomRateSerializer

class RoomRateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomRate.objects.all()
    serializer_class = RoomRateSerializer


# OverriddenRoomRate Views
class OverriddenRoomRateListCreateView(generics.ListCreateAPIView):
    queryset = OverriddenRoomRate.objects.all()
    serializer_class = OverriddenRoomRateSerializer

class OverriddenRoomRateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OverriddenRoomRate.objects.all()
    serializer_class = OverriddenRoomRateSerializer


# Discount Views
class DiscountListCreateView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class DiscountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


# DiscountRoomRate Views
class DiscountRoomRateListCreateView(generics.ListCreateAPIView):
    queryset = DiscountRoomRate.objects.all()
    serializer_class = DiscountRoomRateSerializer


# Lowest Room Rate Calculation
class LowestRoomRateView(APIView):
    serializer_class = RoomRateSerializer

    def get(self, request, *args, **kwargs):
        room_id = self.request.query_params.get('room_id')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        # Ensure room_id is passed and valid
        if not room_id:
            return Response({"error": "room_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            room_rate = RoomRate.objects.get(room_id=room_id)
            
        except RoomRate.DoesNotExist:
            return Response({"error": "RoomRate not found"}, status=status.HTTP_404_NOT_FOUND)

        overridden_rates = OverriddenRoomRate.objects.filter(room_rate=room_rate, stay_date__range=[start_date, end_date])
        discount_room_rates = DiscountRoomRate.objects.filter(room_rate=room_rate)

        rates_with_discounts = []

        for overridden_rate in overridden_rates:
            rate = overridden_rate.overridden_rate
            max_discount_value = 0  # Initialize to 0

            for discount_room_rate in discount_room_rates:
                discount = discount_room_rate.discount
                if discount.discount_type == Discount.PERCENTAGE:
                    discount_value = rate * (discount.discount_value / 100)
                else:
                    discount_value = discount.discount_value

                max_discount_value = max(max_discount_value, discount_value)

            final_rate = rate - max_discount_value
            rates_with_discounts.append(final_rate)

        # If there are no overridden rates, use the default rate
        if not rates_with_discounts:
            rates_with_discounts.append(room_rate.default_rate)

        # Return the minimum value from rates_with_discounts
        response_data = {
            "room_id": room_rate.room_id,
            "room_name": room_rate.room_name,
            "lowest_rate": min(rates_with_discounts),
            "start_date": start_date,
            "end_date": end_date
        }
        return Response(response_data, status=status.HTTP_200_OK)

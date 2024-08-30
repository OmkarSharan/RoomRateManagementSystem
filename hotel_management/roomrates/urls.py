from django.urls import path
from roomrates.views import (
    RoomRateListCreateAPIView, RoomRateRetrieveUpdateDestroyAPIView,
    OverriddenRoomRateListCreateAPIView, OverriddenRoomRateRetrieveUpdateDestroyAPIView,
    DiscountListCreateAPIView, DiscountRetrieveUpdateDestroyAPIView,
    DiscountRoomRateListCreateAPIView, DiscountRoomRateRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('roomrates/', RoomRateListCreateAPIView.as_view(), name='roomrate-list-create'),
    path('roomrates/<int:pk>/', RoomRateRetrieveUpdateDestroyAPIView.as_view(), name='roomrate-detail'),
    path('overriddenrates/', OverriddenRoomRateListCreateAPIView.as_view(), name='overriddenrate-list-create'),
    path('overriddenrates/<int:pk>/', OverriddenRoomRateRetrieveUpdateDestroyAPIView.as_view(), name='overriddenrate-detail'),
    path('discounts/', DiscountListCreateAPIView.as_view(), name='discount-list-create'),
    path('discounts/<int:pk>/', DiscountRetrieveUpdateDestroyAPIView.as_view(), name='discount-detail'),
    path('discountroomrates/', DiscountRoomRateListCreateAPIView.as_view(), name='discountroomrate-list-create'),
    path('discountroomrates/<int:pk>/', DiscountRoomRateRetrieveUpdateDestroyAPIView.as_view(), name='discountroomrate-detail'),
]

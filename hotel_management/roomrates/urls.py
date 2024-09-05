from django.urls import path
from roomrates.views import (
    RoomRateListCreateView, RoomRateDetailView,
    OverriddenRoomRateListCreateView, OverriddenRoomRateDetailView,
    DiscountListCreateView, DiscountDetailView,
    DiscountRoomRateListCreateView,
    LowestRoomRateView
)

urlpatterns = [
    # RoomRate URLs
    path('roomrates/', RoomRateListCreateView.as_view(), name='roomrate-list-create'),
    path('roomrates/<int:pk>/', RoomRateDetailView.as_view(), name='roomrate-detail'),

    # OverriddenRoomRate URLs
    path('overriddenrates/', OverriddenRoomRateListCreateView.as_view(), name='overriddenrate-list-create'),
    path('overriddenrates/<int:pk>/', OverriddenRoomRateDetailView.as_view(), name='overriddenrate-detail'),

    # Discount URLs
    path('discounts/', DiscountListCreateView.as_view(), name='discount-list-create'),
    path('discounts/<int:pk>/', DiscountDetailView.as_view(), name='discount-detail'),

    # DiscountRoomRate URLs
    path('discountroomrates/', DiscountRoomRateListCreateView.as_view(), name='discountroomrate-list-create'),

    # Lowest Room Rate URL
    path('roomrates/lowest/', LowestRoomRateView.as_view(), name='lowest-roomrate'),
]

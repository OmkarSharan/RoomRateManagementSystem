from django.db import models

class RoomRate(models.Model):
    room_id = models.IntegerField(primary_key=True)
    room_name = models.CharField(max_length=100)
    default_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.room_name

class OverriddenRoomRate(models.Model):
    room_rate = models.ForeignKey(RoomRate, on_delete=models.CASCADE)
    overridden_rate = models.DecimalField(max_digits=10, decimal_places=2)
    stay_date = models.DateField()

    def __str__(self):
        return f"{self.room_rate.room_name} - {self.stay_date}"

class Discount(models.Model):
    FIXED = 'fixed'
    PERCENTAGE = 'percentage'

    DISCOUNT_TYPE_CHOICES = [
        (FIXED, 'Fixed'),
        (PERCENTAGE, 'Percentage'),
    ]

    discount_id = models.IntegerField(primary_key=True)
    discount_name = models.CharField(max_length=100)
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_TYPE_CHOICES)
    discount_value = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.discount_name

class DiscountRoomRate(models.Model):
    room_rate = models.ForeignKey(RoomRate, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room_rate.room_name} - {self.discount.discount_name}"

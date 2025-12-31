from rest_framework import serializers
from .models import Room, Seat, Car

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

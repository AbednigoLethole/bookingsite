from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Room, Seat, Car
from .serializers import RoomSerializer, SeatSerializer, CarSerializer


# Create your views here.
@api_view(['GET'])
def all_rooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def all_seats(request):
    seats = Seat.objects.filter(available=True)
    serializer = SeatSerializer(seats, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def all_cars(request):
    cars = Car.objects.filter(available='Y')
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

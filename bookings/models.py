from django.db import models

class Seat(models.Model):
    seat_dest_id = models.CharField(max_length=50, unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.seat_dest_id


class SeatBooking(models.Model):
    STATUS_CHOICES = [
        ('Pending approval', 'Pending approval'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    booker_email = models.EmailField()
    departure_seat = models.ForeignKey(
        Seat, related_name='departure_bookings', 
        on_delete=models.SET_NULL, null=True, blank=True
    )
    return_seat = models.ForeignKey(
        Seat, related_name='return_bookings', 
        on_delete=models.SET_NULL, null=True, blank=True
    )
    reason = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending approval')

    def __str__(self):
        return f"{self.booker_email} - {self.status}"


class Car(models.Model):
    car_registration = models.CharField(primary_key=True, max_length=20)
    car_type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    
    AVAILABLE_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    available = models.CharField(max_length=1, choices=AVAILABLE_CHOICES, default='Y')

    def __str__(self):
        return self.car_registration


class CarBooking(models.Model):
    driver_email = models.EmailField()
    passengers = models.TextField(blank=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    STATUS_CHOICES = (
        ('Pending approval', 'Pending approval'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending approval')

    def __str__(self):
        return f"{self.driver_email} booking"


class Room(models.Model):
    room_id = models.CharField(max_length=20, primary_key=True)
    bed_type = models.CharField(max_length=20)  # 'Single' or 'Double'
    AVAILABLE_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    available = models.CharField(max_length=1, choices=AVAILABLE_CHOICES, default='Y')

    def __str__(self):
        return self.room_id


class RoomBooking(models.Model):
    STATUS_CHOICES = (
        ('Pending approval', 'Pending approval'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    guest_email = models.EmailField()
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending approval')

    def __str__(self):
        return f"{self.guest_email} - {self.status}"

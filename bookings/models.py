from django.db import models

class Seat(models.Model):
    SeatDestID = models.CharField(max_length=50, unique=True)
    Available = models.BooleanField(default=True)

    def __str__(self):
        return self.SeatDestID

class SeatBooking(models.Model):
    STATUS_CHOICES = [
        ('Pending approval', 'Pending approval'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    Booker_Email = models.EmailField()
    Departure_Seat = models.ForeignKey(Seat, related_name='departure_bookings', on_delete=models.SET_NULL, null=True, blank=True)
    Return_Seat = models.ForeignKey(Seat, related_name='return_bookings', on_delete=models.SET_NULL, null=True, blank=True)
    Reason = models.TextField(blank=True)
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending approval')

    def __str__(self):
        return f"{self.Booker_Email} - {self.Status}"


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

    car_registration = models.ForeignKey(
        Car,
        on_delete=models.SET_NULL,   # we can change later depending on rule
        null=True
    )

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

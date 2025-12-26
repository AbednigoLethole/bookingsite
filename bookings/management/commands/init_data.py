# bookings/management/commands/init_data.py
from django.core.management.base import BaseCommand
from bookings.models import Seat, Car

class Command(BaseCommand):
    help = 'Create initial Seat and Car entries'

    def handle(self, *args, **kwargs):
        # Seats
        if not Seat.objects.exists():
            seats = [
                # CPT to LSB (1-8)
                Seat(SeatDestID='CPT_TO_LSB1'), Seat(SeatDestID='CPT_TO_LSB2'),
                Seat(SeatDestID='CPT_TO_LSB3'), Seat(SeatDestID='CPT_TO_LSB4'),
                Seat(SeatDestID='CPT_TO_LSB5'), Seat(SeatDestID='CPT_TO_LSB6'),
                Seat(SeatDestID='CPT_TO_LSB7'), Seat(SeatDestID='CPT_TO_LSB8'),

                # LSB to CPT (9-16)
                Seat(SeatDestID='LSB_TO_CPT1'), Seat(SeatDestID='LSB_TO_CPT2'),
                Seat(SeatDestID='LSB_TO_CPT3'), Seat(SeatDestID='LSB_TO_CPT4'),
                Seat(SeatDestID='LSB_TO_CPT5'), Seat(SeatDestID='LSB_TO_CPT6'),
                Seat(SeatDestID='LSB_TO_CPT7'), Seat(SeatDestID='LSB_TO_CPT8'),

                # HLA to LSB (17-24)
                Seat(SeatDestID='HLA_TO_LSB1'), Seat(SeatDestID='HLA_TO_LSB2'),
                Seat(SeatDestID='HLA_TO_LSB3'), Seat(SeatDestID='HLA_TO_LSB4'),
                Seat(SeatDestID='HLA_TO_LSB5'), Seat(SeatDestID='HLA_TO_LSB6'),
                Seat(SeatDestID='HLA_TO_LSB7'), Seat(SeatDestID='HLA_TO_LSB8'),

                # LSB to HLA (25-32)
                Seat(SeatDestID='LSB_TO_HLA1'), Seat(SeatDestID='LSB_TO_HLA2'),
                Seat(SeatDestID='LSB_TO_HLA3'), Seat(SeatDestID='LSB_TO_HLA4'),
                Seat(SeatDestID='LSB_TO_HLA5'), Seat(SeatDestID='LSB_TO_HLA6'),
                Seat(SeatDestID='LSB_TO_HLA7'), Seat(SeatDestID='LSB_TO_HLA8'),
            ]
            Seat.objects.bulk_create(seats)
            self.stdout.write(self.style.SUCCESS('Seats created'))

        # Cars
        if not Car.objects.exists():
            cars = [
                Car(car_registration='CRG861 NC', car_type='Bakkie', capacity=4, available='Y'),
                Car(car_registration='DBX 736 NC', car_type='Bakkie', capacity=4, available='Y'),
                Car(car_registration='DBX 733 NC', car_type='Bakkie', capacity=4, available='Y'),
                Car(car_registration='WXY 123 NC', car_type='Sedan', capacity=4, available='Y'),
            ]
            Car.objects.bulk_create(cars)
            self.stdout.write(self.style.SUCCESS('Cars created'))

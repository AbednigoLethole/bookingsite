# bookings/management/commands/init_data.py
from django.core.management.base import BaseCommand
from bookings.models import Seat, Car, Room

class Command(BaseCommand):
    help = 'Create initial Seat, Car, and Room entries'

    def handle(self, *args, **kwargs):
        # Seats
        if not Seat.objects.exists():
            seats = [
                # CPT to LSB (1-8)
                Seat(seat_dest_id='CPT_TO_LSB1'), Seat(seat_dest_id='CPT_TO_LSB2'),
                Seat(seat_dest_id='CPT_TO_LSB3'), Seat(seat_dest_id='CPT_TO_LSB4'),
                Seat(seat_dest_id='CPT_TO_LSB5'), Seat(seat_dest_id='CPT_TO_LSB6'),
                Seat(seat_dest_id='CPT_TO_LSB7'), Seat(seat_dest_id='CPT_TO_LSB8'),

                # LSB to CPT (9-16)
                Seat(seat_dest_id='LSB_TO_CPT1'), Seat(seat_dest_id='LSB_TO_CPT2'),
                Seat(seat_dest_id='LSB_TO_CPT3'), Seat(seat_dest_id='LSB_TO_CPT4'),
                Seat(seat_dest_id='LSB_TO_CPT5'), Seat(seat_dest_id='LSB_TO_CPT6'),
                Seat(seat_dest_id='LSB_TO_CPT7'), Seat(seat_dest_id='LSB_TO_CPT8'),

                # HLA to LSB (17-24)
                Seat(seat_dest_id='HLA_TO_LSB1'), Seat(seat_dest_id='HLA_TO_LSB2'),
                Seat(seat_dest_id='HLA_TO_LSB3'), Seat(seat_dest_id='HLA_TO_LSB4'),
                Seat(seat_dest_id='HLA_TO_LSB5'), Seat(seat_dest_id='HLA_TO_LSB6'),
                Seat(seat_dest_id='HLA_TO_LSB7'), Seat(seat_dest_id='HLA_TO_LSB8'),

                # LSB to HLA (25-32)
                Seat(seat_dest_id='LSB_TO_HLA1'), Seat(seat_dest_id='LSB_TO_HLA2'),
                Seat(seat_dest_id='LSB_TO_HLA3'), Seat(seat_dest_id='LSB_TO_HLA4'),
                Seat(seat_dest_id='LSB_TO_HLA5'), Seat(seat_dest_id='LSB_TO_HLA6'),
                Seat(seat_dest_id='LSB_TO_HLA7'), Seat(seat_dest_id='LSB_TO_HLA8'),
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

        # Rooms
        if not Room.objects.exists():
            rooms = [
                # KFH1 Block
                Room(room_id='KFH1RM1', bed_type='Single', available='Y'),
                Room(room_id='KFH1RM2', bed_type='Double', available='Y'),
                Room(room_id='KFH1RM3', bed_type='Single', available='Y'),
                Room(room_id='KFH1RM4', bed_type='Double', available='Y'),

                # KFH3 Block
                Room(room_id='KFH3RM1', bed_type='Single', available='Y'),
                Room(room_id='KFH3RM2', bed_type='Single', available='Y'),
                Room(room_id='KFH3RM3', bed_type='Double', available='Y'),
                Room(room_id='KFH3RM4', bed_type='Double', available='Y'),

                # LBH1 Block
                Room(room_id='LBH1RM1', bed_type='Double', available='Y'),
                Room(room_id='LBH1RM2', bed_type='Double', available='Y'),
                Room(room_id='LBH1RM3', bed_type='Single', available='Y'),
                Room(room_id='LBH1RM4', bed_type='Double', available='Y'),
                Room(room_id='LBH1RM5', bed_type='Single', available='Y'),
            ]
            Room.objects.bulk_create(rooms)
            self.stdout.write(self.style.SUCCESS("13 rooms successfully created!"))

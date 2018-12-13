from rest_framework import generics
from api.models import User, Superadmin, Subadmin, Borrower, Facility, Equipment, Reservation, Schedule, Logs
from api.serializers import UserSerializer, SuperadminSerializer, SubadminSerializer, BorrowerSerializer, FacilitySerializer, EquipmentSerializer, ReservationSerializer, ScheduleSerializer, LogsSerializer

# TOKEN

# class TokenList(generics.ListCreateAPIView):
#     queryset = Token.objects.all()
#     serializer_class = TokenSerializer

# USER

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# SUPERADMIN

class SuperadminList(generics.ListCreateAPIView):
    serializer_class = SuperadminSerializer

    def get_queryset(self):
        queryset = Superadmin.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset

class SuperadminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Superadmin.objects.all()
    serializer_class = SuperadminSerializer

# SUBADMIN

class SubadminList(generics.ListCreateAPIView):
    serializer_class = SubadminSerializer

    def get_queryset(self):
        queryset = Subadmin.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset

class SubadminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subadmin.objects.all()
    serializer_class = SubadminSerializer

# BORROWER

class BorrowerList(generics.ListCreateAPIView):
    serializer_class = BorrowerSerializer

    def get_queryset(self):
        queryset = Borrower.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset

class BorrowerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

# FACILITY

class FacilityList(generics.ListCreateAPIView):
    serializer_class = FacilitySerializer

    def get_queryset(self):
        queryset = Facility.objects.all()
        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset

class FacilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

# EQUIPMENT

class EquipmentList(generics.ListCreateAPIView):
    serializer_class = EquipmentSerializer

    def get_queryset(self):
        queryset = Equipment.objects.all()
        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset

class EquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


# RESERVATION

class ReservationList(generics.ListCreateAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = Reservation.objects.all()
        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(borrower_id=user)
        rtype = self.request.query_params.get('type', None)
        if rtype is not None:
            queryset = queryet.filter(reserve_type=rtype)
        month = self.request.query_params.get('month', None)
        if month is not None:
            queryset = queryset.filter(month=month)
        return queryset

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# SCHEDULE

class ScheduleList(generics.ListCreateAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        queryset = Schedule.objects.all()
        item_type = self.request.query_params.get('item_type', None)
        if item_type is not None:
            queryset = queryset.filter(item_type=item_type)
        item_id = self.request.query_params.get('item_id', None)
        if item_id is not None:
            queryset = queryset.filter(item_id=item_id)
        year = self.request.query_params.get('year', None)
        if year is not None:
            queryset = queryset.filter(year=year)
        month = self.request.query_params.get('month', None)
        if month is not None:
            queryset = queryset.filter(month=month)
        day = self.request.query_params.get('day', None)
        if day is not None:
            queryset = queryset.filter(day=day)
        return queryset

class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ScheduleSerializer

# LOGS

class LogsList(generics.ListCreateAPIView):
    serializer_class = LogsSerializer

    def get_queryset(self):
        queryset = Logs.objects.all()
        date = self.request.query_params.get('date', None)
        if date is not None:
            queryset = queryset.filter(date=date)
        borrower = self.request.query_params.get('borrower', None)
        if borrower is not None:
            queryset = queryset.filter(borrower=borrower)
        admin = self.request.query_params.get('admin', None)
        if admin is not None:
            queryset = queryset.filter(admin=admin)
        return queryset

class LogsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
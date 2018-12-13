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
from rest_framework import generics, viewsets,status
from social_django.utils import load_strategy
from api.models import *
from api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render_to_response, redirect, render, get_object_or_404, redirect
import json,requests
# from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
from django.template.context import RequestContext
# from django_oauth2.decorators import resource
# from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# TOKEN

class TokenList(generics.ListCreateAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

# SUPERADMIN

class SuperadminList(generics.ListCreateAPIView):
    serializer_class = SuperadminSerializer

    def get_queryset(self):
        queryset = Superadmin.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset

    queryset = Superadmin.objects.all()
    serializer_class = SuperadminSerializer

>>>>>>> efe705913766d19453f8b66ff93a10674be0450f
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

    queryset = Subadmin.objects.all()
    serializer_class = SubadminSerializer

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
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer


class BorrowerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

# FACILITY

class FacilityList(generics.ListCreateAPIView):
#FACILITY
class FacilityListss(generics.ListCreateAPIView):
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
class FacilityDetailss(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
#ADD NEW AND SHOW ALL FACILITIES
@api_view(['GET', 'POST'])
def FacilityList(request):
    #dumping request.data in an array
    jsonList = [] 
    jsonList.append(request.data)
    print(jsonList)
    
    #SHOW ALL FACILITIES 1 AND 0 STATUS
    if request.method == 'GET':
        queryset = Facility.objects.all()
        serializer_class = FacilitySerializer(queryset, many=True)
        print(serializer_class.data)
        return JsonResponse({"data":serializer_class.data})
    
    #ADD NEW FACILITIES 
    elif request.method == 'POST':
        c = jsonList[0]['name']
        search = Facility.objects.filter(name__iexact = c)  #checking if enetered name is already in db
        if search:
            return Response("Facility alredy exist")
        else:
            queryset = FacilitySerializer(data=request.data)
            if queryset.is_valid():
                queryset.save()
                return Response(queryset.data, status=status.HTTP_201_CREATED)
            return Response(queryset.errors, status=status.HTTP_400_BAD_REQUEST)

#GET ALL AVAILABLE FACILITIES
@api_view(['GET'])
def Facilityavailable(request):
    queryset = Facility.objects.filter(status = 1).all()
    serializer_class = FacilitySerializer(queryset, many=True)
    return Response(serializer_class.data)

#GET ALL UNAVAILABLE FACILITIES
@api_view(['GET'])
def FacilityUnavailable(request):
    queryset = Facility.objects.filter(status = 0).all()
    serializer_class = FacilitySerializer(queryset, many=True)
    return Response(serializer_class.data)

#EDIT particular facilitiy
@api_view(['POST'])
def FacilityEdit(request,pk):
    jsonlist = []
    jsonlist.append(request.data)
    print("dasdkashdkshkjdhaskhdjashdkjhskhdkashdkjashdk")
    print(jsonlist)
    queryset = Facility.objects.filter(id = pk)
    print(queryset)
    if queryset:
        if jsonlist[0]['name'] == '':
            queryset[0].name = queryset[0].name
            queryset[0].save()
        else:
            queryset[0].name = jsonlist[0]['name']
            queryset[0].save()

        if jsonlist[0]['status'] == '':
            pass
            # queryset[0].status = queryset[0].status
            # queryset[0].save()

        else:
            queryset[0].status = jsonlist[0]['status']
            queryset[0].save()

        if jsonlist[0]['quantity'] == '':
            queryset[0].quantity = queryset[0].quantity
            queryset[0].save()

        else:
            queryset[0].quantity = jsonlist[0]['quantity']
            queryset[0].save()

        return Response("Updated")
    else:
        return Response("Facility doesn't exist")

#CHANGE STATUS OF FACILITIES TO UNVAILABLE
@api_view(['POST'])
def Facilitystatus0(request,pk):
    # jsonList = []
    # jsonList.append(request.data)
    # name = jsonList[0]['name']
    print(pk)
    queryset = Facility.objects.filter(status = 1 ).filter(id = pk)
    if queryset:
        queryset[0].status = 0
        queryset[0].save()
        return Response('Status changed!')
    else:
        return Response('Not found!')

#CHANGE STATUS OF FACILITIES TO AVAILABLE
@api_view(['POST'])
def Facilitystatus1(request,pk):
    # jsonList = []
    # jsonList.append(request.data)
    # name = jsonList[0]['name']
    queryset = Facility.objects.filter(status = 0 ).filter(id = pk)
    if queryset:
        queryset[0].status = 1
        queryset[0].save()
        return Response('Status changed!')
    else:
        return Response('Not found!')

#ADD QUANTITY IN FACILITIES
@api_view(['POST'])
def Facilityquantity(request):
    jsonList = []
    jsonList.append(request.data)
    newquantity = jsonList[0]['quantity']
    name = jsonList[0]['name']
    if isinstance(newquantity, str) == True: #check if the entered quantity is in int or str
        return Response('please enter valid number of quantity')
    else:
        queryset = Facility.objects.filter(status = 1 ).filter(name__iexact = name)
        if queryset:
            queryset[0].quantity = queryset[0].quantity + newquantity 
            queryset[0].save()
            return Response('New Facility/s added!')
        else:
            return Response('Not found!')


# EQUIPMENT

@api_view(['GET', 'POST'])
def EquipmentList(request):
    jsonList = []
    jsonList.append(request.data)
    
    #SHOW ALL EQUIPMENTS 1 AND 0 STATUS
    if request.method == 'GET':
        queryset = Equipment.objects.all()
        serializer_class = EquipmentSerializer(queryset, many=True)
        return Response(serializer_class.data)
    
    #ADD NEW EQUIPMENT 
    elif request.method == 'POST':
        c = jsonList[0]['name']
        search = Equipment.objects.filter(name__iexact = c)
        if search:
            return Response("Equipment alredy exist")
        else:
            queryset = EquipmentSerializer(data=request.data)
            if queryset.is_valid():
                queryset.save()
                return Response(queryset.data, status=status.HTTP_201_CREATED)
            return Response(queryset.errors, status=status.HTTP_400_BAD_REQUEST)

#GET ALL AVAILABLE EQUIPMENTS
@api_view(['GET'])
def Equipmentavailable(request):
    queryset = Equipment.objects.filter(status = 1).all()
    serializer_class = EquipmentSerializer(queryset, many=True)
    return Response(serializer_class.data)

#GET ALL UNAVAILABLE EQUIPMENTS
@api_view(['GET'])
def EquipmentUnavailable(request):
    queryset = Equipment.objects.filter(status = 0).all()
    serializer_class = EquipmentSerializer(queryset, many=True)
    return Response(serializer_class.data)

#EDIT particular facilitiy
@api_view(['POST'])
def EquipmentEdit(request):
    jsonlist = []
    jsonlist.append(request.data)

    queryset = Equipment.objects.filter(name__iexact = jsonlist[0]['name'])
    print(queryset)
    if queryset:
        if jsonlist[0]['name'] == '':
            queryset[0].name = queryset[0].name
        else:
            queryset[0].name = jsonlist[0]['name']

        if jsonlist[0]['status'] == '':
            queryset[0].status = queryset[0].status
        else:
            queryset[0].status = jsonlist[0]['status']

        if jsonlist[0]['quantity'] == '':
            queryset[0].quantity = queryset[0].quantity
        else:
            queryset[0].quantity = jsonlist[0]['quantity']
        return Response("Updated")
    else:
        return Response("Equipment doesn't exist")

#CHANGE STATUS OF EQUIPMNT TO UNVAILABLE
@api_view(['POST'])
def Equipmentstatus0(request):
    jsonList = []
    jsonList.append(request.data)
    name = jsonList[0]['name']
    print(name)
    queryset = Equipment.objects.filter(status = 1 ).filter(name__iexact = name)
    # print(queryset[0].status)
    if queryset:
        queryset[0].status = 0
        queryset[0].save()
    # serializer_class = EquipmentSerializer(queryset, many=True)
        return Response('Status changed!')
    else:
        return Response('Not found!')

#CHANGE STATUS OF EQUIPMNT TO AVAILABLE
@api_view(['POST'])
def Equipmentstatus1(request):
    jsonList = []
    jsonList.append(request.data)
    name = jsonList[0]['name']
    print(name)
    queryset = Equipment.objects.filter(status = 0 ).filter(name__iexact = name)
    # print(queryset[0].status)
    if queryset:
        queryset[0].status = 1
        queryset[0].save()
    # serializer_class = EquipmentSerializer(queryset, many=True)
        return Response('Status changed!')
    else:
        return Response('Not found!')

#ADD QUANTITY IN EQUIPMENTS
@api_view(['POST'])
def Equipmentquantity(request):
    jsonList = []
    jsonList.append(request.data)
    newquantity = jsonList[0]['quantity']
    name = jsonList[0]['name']
    print(name)
    print(newquantity)
    queryset = Equipment.objects.filter(status = 1 ).filter(name__iexact = name)
    # print(queryset[0].status)
    if queryset:
        queryset[0].quantity = queryset[0].quantity + newquantity 
        queryset[0].save()
    # serializer_class = EquipmentSerializer(queryset, many=True)
        return Response('New equipment/s added!')
    else:
        return Response('Not found!')


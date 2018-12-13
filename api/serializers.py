<<<<<<< HEAD
from .models import User, Superadmin, Subadmin, Borrower, Facility, Equipment, Reservation, Schedule, Logs
from rest_framework import serializers

# class TokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Token
#         fields = ('id', 'token', 'ttl')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'date_added' ,'email', 'usertype',)

from .models import *
from rest_framework import serializers

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('id', 'token', 'ttl')
        
class SuperadminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superadmin
        fields = ('id', 'name', 'email', 'token_id')

    # THIS IS SAMPLE CODE FOR USING serializers.Serializers

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True, allow_blank=False, max_length=70)
    # email = serializers.CharField(required=True, allow_blank=False, max_length=70)
    # token_id = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    # def create(self, validated_data):
    #     return Superadmin.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance

    # END OF SAMPLE

class SubadminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subadmin
        fields = ('id', 'name', 'email', 'token_id')

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True, allow_blank=False, max_length=70)
    # email = serializers.CharField(required=True, allow_blank=False, max_length=70)
    # token_id = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    # def create(self, validated_data):
    #     return Subadmin.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ('id', 'name', 'email', 'token_id')

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ('id', 'name', 'description', 'image', 'status', 'date_added','borrower_id')
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True, allow_blank=False, max_length=70)
    # email = serializers.CharField(required=True, allow_blank=False, max_length=70)
    # token_id = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    # def create(self, validated_data):
    #     return Borrower.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ('id', 'name', 'status', 'date_added','borrower_id', 'quantity')

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'name', 'description', 'image', 'status', 'quantity', 'date_added', 'borrower_id')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'borrower_id', 'item_id', 'reserve_type', 'eventname', 'quantity', 'date_application', 'year', 'month', 'start_day', 'end_day', 'start_time', 'end_time', 'remarks', 'status')

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'info', 'day', 'month', 'year', 'time_start', 'time_end', 'item_type', 'item_id')

class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = ('id', 'date', 'borrower', 'admin', 'message') 
        fields = ('id', 'name', 'status', 'date_added', 'borrower_id', 'quantity')
        # fields = ('id', 'name', 'status', 'date_added', 'quantity')


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('Reserver_ID','Status','Cancelled','Type','Name_reserved','Date_Resereved','Date_Return')
class BorrowerLogsSerializer(serializers.ModelSerializer):
    class Meta:
        fields =('Borrower_ID','Approver_ID','Type','Name_Borrowed','Date_Borrowed','Date_Return')
    
class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        fields =('User_ID','action','Date')



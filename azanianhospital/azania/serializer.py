from rest_framework import serializers
from .models import patient, doctor, appointments, User


class patientSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient
        fields = ("id", "patient_name", "patient_lastname")

class doctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = ("id", "doctor_name", "doctor_lastname")

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointments
        fields = ("id", "doctor_name", "patient_name", "date")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username","email", "password")
        extra_kwargs = {'password': {'write_only': True}}

    def create (self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



# Create your views here.
from rest_framework import generics
from .models import patient, doctor, appointments, User
from .serializer import patientSerializer, doctorSerializer, AppointmentSerializer, UserSerializer
from django.http import request



"""
#placeholder view functions. Will be connected to urls.py
class ListPatients(generics.ListAPIView):
#def patients(request):
    queryset = patient.objects.all()
    serializer_class = patientSerializer

class ListDoctors(generics.ListAPIView):
    queryset = doctor.objects.all()
    serializer_class = doctorSerializer

class  ListAppointments(generics.ListAPIView):
    queryset = appointments.objects.all()
    serializer_class = AppointmentSerializer
"""
#Views to be used in the url requests

class AddUser(generics.CreateAPIView ):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeleteUser(generics.RetrieveDestroyAPIView):
    #pk = User.objects.get.only('id')
    queryset = User.objects.all()
    serializer_class = UserSerializer

class  AddAppointment(generics.CreateAPIView):
    queryset = appointments.objects.all()
    serializer_class = AppointmentSerializer

class  DeleteAppointment(generics.RetrieveDestroyAPIView):
    queryset = appointments.objects.all()
    serializer_class = AppointmentSerializer

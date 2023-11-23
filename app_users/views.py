from django.shortcuts import render
from .models import Patient,Tests,Sample,Doctor,Result
from .serializers import PatientSerializer,TestsSerializer,SampleSerializer,DoctorSerializer,ResultSerializer
from rest_framework import generics

class PatientListView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class PatientDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class TestsListView(generics.ListCreateAPIView):
    serializer_class = TestsSerializer
    queryset = Tests.objects.all()

class TestsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TestsSerializer
    queryset = Tests.objects.all()

class SampleListView(generics.ListCreateAPIView):
    serializer_class = SampleSerializer
    queryset = Sample.objects.all()

class SampleDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SampleSerializer
    queryset = Sample.objects.all()

class DoctorListView(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class DoctorDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class ResultListView(generics.ListCreateAPIView):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()

class ResultDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()
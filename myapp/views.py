from myapp.models import Register
from myapp.serializers import RegisterSerializer
from rest_framework import generics, viewsets
from django.shortcuts import render


class RegisterList(generics.ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer


class RegisterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer


def show(request):
	obj = Register.objects.all()
	return render(request, "myapp/show.html", {"obj" : obj})
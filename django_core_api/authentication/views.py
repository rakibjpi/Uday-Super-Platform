# django_core_api/authentication/views.py
from django.forms import models
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User

from . import models
from . import serializers


@api_view(['GET'])
def users(request):
    users = User.objects.all()
    serializer = serializers.UserSerializer(users, many=True)
    return Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
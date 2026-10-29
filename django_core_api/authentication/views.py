# django_core_api/authentication/views.py
from django.forms import models
from django.shortcuts import render

# Create your views here.
from httpx import request
from rest_framework import viewsets

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from . import models
from . import serializers
from . import permissions

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    
    # Apply permissions dynamically based on your exact logic:
    # Option A: Anyone can GET, but only Authenticated users can write.
    # permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Option B: Anyone can GET, but only Admins can write (Recommended for general User lists).
    permission_classes = [permissions.IsAdminOrReadOnly]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]

        
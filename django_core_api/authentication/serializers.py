# django_core_api/authentication/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '_all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        # Correctly hash the password when an authorized user creates a new account
        return User.objects.create_user(**validated_data)
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ['id', 'employee', 'department', 'position']
        read_only_fields = ['id']
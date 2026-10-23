# django_core_api/authentication/models.py
from django.db import models

# Create your models here.
from django.contrib.auth.models import Group, User

class RoleLayer(Group):
    description = models.TextField(blank=True, null=True)    
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
            verbose_name = 'Role Layer'
            verbose_name_plural = 'Role Layers'

    def __str__(self):
        return self.name
    
class RoleChoices(models.TextChoices):
    SYSTEM_ADMIN = 'system_admin', 'System Admin'
    SUPER_ADMIN = 'super_admin', 'Super Admin'
    ADMIN = 'admin', 'Admin'
    USER = 'user', 'User'
    GUEST = 'guest', 'Guest'

class UserRole(models.Model):
    name = models.CharField(max_length=100, choices=RoleChoices.choices)
    layer = models.ForeignKey(RoleLayer, on_delete=models.CASCADE, related_name='roles')
    description = models.TextField(blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
            verbose_name = 'User Role'
            verbose_name_plural = 'User Roles'

    def __str__(self):
        return self.layer.name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
            verbose_name = 'User Profile'
            verbose_name_plural = 'User Profiles'
            
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Employee(models.Model):
    employee = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        
    def __str__(self):
        return f"{self.employee.user.first_name} {self.employee.user.last_name}"
    
    
# django_core_api/authentication/admin.py
from django.contrib import admin

from . import models

@admin.register(models.RoleLayer)
class RoleLayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'added_at', 'updated_at')
    search_fields = ('name', 'description')

@admin.register(models.UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'layer', 'description', 'added_at', 'updated_at')
    search_fields = ('name', 'layer__name', 'description')
    
@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'added_at', 'updated_at')
    search_fields = ('user__username', 'user__email')
    
@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'department', 'position', 'added_at', 'updated_at')
    search_fields = ('employee__user__username', 'employee__user__email', 'department', 'position')
    
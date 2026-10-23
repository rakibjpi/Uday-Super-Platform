# django_core_api/authentication/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet, basename='employee')

from . import views
urlpatterns = [
    path('users/', views.users, name='users'),
    path('',  include(router.urls)),
    
]
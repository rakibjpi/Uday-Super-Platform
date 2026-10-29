# django_core_api/authentication/urls.py
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'employees', views.EmployeeViewSet, basename='employee')

from . import views
urlpatterns = [
    path('',  include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('api/token/', obtain_auth_token, name='token_obtain_pair'),
    
]
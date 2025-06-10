from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import home
from config.views import home, dashboard  # Make sure 'dashboard' is included

# Import ViewSets from each app
from employees.views import EmployeeViewSet
from departments.views import DepartmentViewSet
from attendance.views import AttendanceViewSet
from performance.views import PerformanceViewSet
from departments.views import EmployeeCountByDepartment
from attendance.views import MonthlyAttendance

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet)

# Swagger Schema
schema_view = get_schema_view(
   openapi.Info(
      title="Employee Management System API",
      default_version='v1',
      description="API documentation for Employee Management System",
      terms_of_service="https://www.google.com/policies/terms/", 
      contact=openapi.Contact(email="contact@yourproject.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/department-employee-count/', EmployeeCountByDepartment.as_view()),
    path('api/monthly-attendance/', MonthlyAttendance.as_view()),
    path('dashboard/', dashboard), 

        # Swagger URLs
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('login.urls')),
    
    
    
]

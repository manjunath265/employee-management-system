from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Department
from .serializers import DepartmentSerializer
from employees.models import Employee
from django.db.models import Count
from rest_framework.permissions import AllowAny

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeCountByDepartment(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        departments = Department.objects.annotate(employee_count=Count('employee'))
        data = {dept.name: dept.employee_count for dept in departments}
        return Response(data)
from rest_framework import viewsets
from .models import Attendance
from .serializers import AttendanceSerializer
from rest_framework.permissions import AllowAny

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Attendance
from django.db.models import Count
from django.utils import timezone
from datetime import datetime

class MonthlyAttendance(APIView):
    permission_classes = [AllowAny] 
    def get(self, request):
        # Get attendance data grouped by year-month
        data = (
            Attendance.objects.extra(select={'month': "TO_CHAR(date, 'YYYY-MM')"})
            .values('month')
            .annotate(present=Count('id', filter=models.Q(status='present')))
            .annotate(absent=Count('id', filter=models.Q(status='absent')))
            .annotate(late=Count('id', filter=models.Q(status='late')))
            .order_by('month')
        )

        labels = []
        present_data = []
        absent_data = []
        late_data = []

        for entry in data:
            labels.append(entry['month'])
            present_data.append(entry['present'])
            absent_data.append(entry['absent'])
            late_data.append(entry['late'])

        return Response({
            "labels": labels,
            "present": present_data,
            "absent": absent_data,
            "late": late_data
        })
"""
Employees views
"""

from rest_framework import viewsets
from .serializers import EmployeeSerializer
from .models import Employee


class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows employees to be viewed only.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

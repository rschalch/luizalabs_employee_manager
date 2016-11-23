"""
Serializers for employees
"""

from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializing Employees
    """
    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')

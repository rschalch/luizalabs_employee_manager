"""
Employees models
"""

from django.db import models


class Employee(models.Model):
    """
    Employee
    """
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name

from django.db import models
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Employee(models.Model):
    ROLES = [
        ('hr', 'HR'),
        ('tl', 'Team Lead'),
        ('fd', 'Frontend Developer'),
        ('bd', 'Backend Developer'),
        ('fr', 'Full Stack Developer'),
    ]
    emp_id=models.UUIDField(primary_key=True,default=uuid4,editable=False)
    emp_name=models.CharField(max_length=255,)
    emp_email=models.CharField(max_length=255,unique=True)
    emp_role=models.CharField(max_length=2,choices=ROLES,default='fd')
    emp_phno=models.IntegerField(
        validators=[
            MaxValueValidator(limit_value=9999999999,message='Phone number must be at least 10 digits.'),
            MinValueValidator(limit_value=1000000000,message='Phone number must be at least 10 digits.')
        ],
    )
    
    def clean(self):
        super().clean()
        if self.emp_role not in dict(self.ROLES):
            raise ValueError('Invalid role.')
        if Employee.objects.filter(emp_id=self.emp_id).exists():
            raise ValueError('ID already exists.')
        if Employee.objects.filter(emp_email=self.emp_email).exists():
            raise ValueError('Email already exists.')
        
    def __str__(self):
        return f'{self.emp_name} - {self.emp_email}'
    
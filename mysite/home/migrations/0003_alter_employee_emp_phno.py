# Generated by Django 5.0 on 2023-12-14 07:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_employee_emp_phno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_phno',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=9999999999, message='Phone number must be at least 10 digits.'), django.core.validators.MinValueValidator(limit_value=1000000000, message='Phone number must be at least 10 digits.')]),
        ),
    ]
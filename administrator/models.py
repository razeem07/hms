from django.db import models

# Create your models here.


class Department(models.Model):
    id=models.BigAutoField(primary_key=True)
    department_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/departments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Set when created
    updated_at = models.DateTimeField(auto_now=True)      # Updated on save


    class Meta:
        db_table='departments'

    def __str__(self):
        return self.department_name


class HealthPackage(models.Model):
    id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/healthpackage/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Set when created
    updated_at = models.DateTimeField(auto_now=True)      # Updated on save


    class Meta:
        db_table='package'

    def __str__(self):
        return self.name


class Insurance(models.Model):
    id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/insurance/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Set when created
    updated_at = models.DateTimeField(auto_now=True)      # Updated on save


    class Meta:
        db_table='insurance'

    def __str__(self):
        return self.name
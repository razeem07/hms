from django.db import models

# Create your models here.

class ContactRequest(models.Model):
     id=models.BigAutoField(primary_key=True)
     first_name=models.CharField(max_length=50)
     last_name=models.CharField(max_length=50)
     email=models.EmailField(max_length=100)
     phone_number=models.CharField(max_length=15,blank=True,null=True)
     message=models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)


     class Meta:
        db_table="contact_request"


     def __str__(self):
          return f"{self.id} {self.first_name} {self.last_name}"
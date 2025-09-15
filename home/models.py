from django.db import models
# from home.models import Contact   # ✅ correct


# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=122)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    description=models.TextField()
    date=models.DateField()
  
    def __str__(self):
      return self.name
  
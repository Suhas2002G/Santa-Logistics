from django.db import models
from django.contrib.auth.models import User     #imported for cart functinality



# Create your models here.
class Gifts(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    gdetails=models.CharField(max_length=100, verbose_name='Product Detail')
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to='image')
from django.db import models

# Create your models here.
from django.db import models

class Mobile(models.Model):
    brand_name = models.TextField(default='Unknown Brand')
    budget_range = models.TextField(default='Unknown')
    name_phone = models.TextField(default  = 'Unknown Brand' )

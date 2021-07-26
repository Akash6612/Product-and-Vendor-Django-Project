from django.db import models

# Create your models here.
class Vendor(models.Model):
    name=models.CharField(max_length=40)
    balance=models.IntegerField()
    address=models.CharField(max_length=50)

    class Meta:
        db_table='Vendor_Info'
        
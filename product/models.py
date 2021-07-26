from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=40)
    price=models.FloatField()
    qty=models.IntegerField()
    review=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images/' ,default='NA',null=True)

    class Meta:
        db_table='Product_Info'

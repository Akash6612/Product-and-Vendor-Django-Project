from django.db.models import fields
from rest_framework import serializers
from .models import Product

class Productserializers(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__' 
        #fields=('name','price')
from django.shortcuts import render
from .models import Product
from .Serializers import Productserializers
from rest_framework.viewsets import ModelViewSet

class ProductOperation(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Productserializers




from django.shortcuts import render
from .models import Vendor
from .Serializers import Vendorserializers
from rest_framework.viewsets import ModelViewSet

class VendorOperation(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = Vendorserializers


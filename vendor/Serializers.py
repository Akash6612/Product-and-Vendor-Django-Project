
from rest_framework import serializers
from .models import Vendor

class Vendorserializers(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__' 
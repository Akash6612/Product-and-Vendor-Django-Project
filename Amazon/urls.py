
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls.conf import include
from rest_framework import views
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Product_Vendor_api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',include('product.producturl')),
    path('vendor/',include('vendor.vendorurl')),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^$', schema_view),
    
    
]

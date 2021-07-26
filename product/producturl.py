from rest_framework import routers
from .views import ProductOperation
from rest_framework import routers

router = routers.SimpleRouter()
router.register('v1',ProductOperation)
urlpatterns=router.urls


from rest_framework import routers
from .views import VendorOperation
router = routers.SimpleRouter()

router.register('v1',VendorOperation)
urlpatterns=router.urls
urlpatterns = router.urls

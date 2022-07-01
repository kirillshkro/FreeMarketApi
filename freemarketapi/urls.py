from rest_framework.routers import DefaultRouter
from freemarketapi.views import *

router = DefaultRouter()

router.register('users', viewset=MarketUserViewSet)
router.register('products', viewset=ProductViewSet)

urlpatterns = router.urls

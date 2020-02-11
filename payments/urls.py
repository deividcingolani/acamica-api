from .views import (
    DueViewSet, PaymentViewSet, TypePaymentViewSet    
)

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('types', TypePaymentViewSet,
                basename='types')
router.register('dues', DueViewSet,
                basename='dues')
router.register('', PaymentViewSet, basename='payments')


urlpatterns = router.urls

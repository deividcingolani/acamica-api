from .views import (
    DueViewSet, PaymentViewSet, TypePaymentViewSet    
)

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('payments/types', TypePaymentViewSet,
                basename='types')
router.register('payments/dues', DueViewSet,
                basename='dues')
router.register('payments', PaymentViewSet, basename='payments')


urlpatterns = router.urls

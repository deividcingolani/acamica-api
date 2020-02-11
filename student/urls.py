from .views import (
    StudentViewSet, CareerViewSet, CountriesViewSet, CitiesViewSet    
)

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('careers', CareerViewSet,
                basename='careers')
router.register('countries', CountriesViewSet, basename='countries')
router.register('cities', CitiesViewSet, basename='cities')
router.register('students', StudentViewSet,
                basename='students')

urlpatterns = router.urls

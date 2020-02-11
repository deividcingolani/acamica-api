from rest_framework import viewsets

from .models import (Student, Career, Countries,
                     Cities
                     )
from .serializers import (StudentSerializer,
                          CareerSerializer,
                          CountriesSerializer,
                          CitiesSerializer
                          )


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    
class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer

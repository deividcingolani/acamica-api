from rest_framework import serializers
from .models import (Student, Career, Countries,
                     Cities,
                     )

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'

class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'

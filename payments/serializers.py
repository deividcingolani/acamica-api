from rest_framework import serializers
from .models import (
         Type_Payment, Payment, Dues_Option
)


class PaymentSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='student.name', label="name")
    email = serializers.ReadOnlyField(source='student.email')
    paymentDescription = serializers.ReadOnlyField(source='payment_type.description')
    dues_value = serializers.ReadOnlyField(source='dues.value')
    country = serializers.ReadOnlyField(source='student.country.description')
    city = serializers.ReadOnlyField(source='student.city.description')
    career = serializers.ReadOnlyField(source='student.career.description')

    class Meta:
        model = Payment
        fields = ('student', 'name',
        'payment_type', 'paymentDescription',
         'dues', 'dues_value',
         'email', 'country', 
         'city', 'id',
         'career')


class TypePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_Payment
        fields = '__all__'

class DueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dues_Option
        fields = '__all__'

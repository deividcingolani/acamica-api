from rest_framework import viewsets

from .models import (Dues_Option, Type_Payment, Payment)
from .serializers import (DueSerializer,
                          TypePaymentSerializer,
                          PaymentSerializer
                          )


class DueViewSet(viewsets.ModelViewSet):
    queryset = Dues_Option.objects.all()
    serializer_class = DueSerializer
    
class TypePaymentViewSet(viewsets.ModelViewSet):
    queryset = Type_Payment.objects.all()
    serializer_class = TypePaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
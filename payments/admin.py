from django.contrib import admin
from .models import (Type_Payment, Dues_Option,
                     Payment,
                     )
from related_admin import RelatedFieldAdmin

class TypeAdmin(admin.ModelAdmin):
    list_display = ('description', 'code' )

class DueAdmin(admin.ModelAdmin):
    list_display = ('value', 'code' )

class PaymentAdmin(RelatedFieldAdmin):
    list_display = ['student__name','payment_type__description', 'dues__value']
    list_filter = ('student__name','payment_type__description')


admin.site.register(Type_Payment, TypeAdmin)
admin.site.register(Payment, PaymentAdmin )
admin.site.register(Dues_Option, DueAdmin)
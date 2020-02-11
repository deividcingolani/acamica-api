from django.contrib import admin

from .models import (Student, Career, Countries,
                     Cities
                     )

admin.site.register(Student)
admin.site.register(Career)
admin.site.register(Countries)
admin.site.register(Cities)
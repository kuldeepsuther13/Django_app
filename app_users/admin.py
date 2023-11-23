from django.contrib import admin
from .models import Patient,Tests,Sample,Doctor,Result

admin.site.register(Patient)
admin.site.register(Tests)
admin.site.register(Sample)
admin.site.register(Doctor)
admin.site.register(Result)

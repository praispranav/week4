from django.contrib import admin
# from .models import related modelfrom 
from .models import cardealer, carmake, carmodel, carreview

admin.site.register(carreview)
admin.site.register(carmodel)
admin.site.register(cardealer)
admin.site.register(carmake)

# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here

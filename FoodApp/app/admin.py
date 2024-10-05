from django.contrib import admin
from .models import FoodApp
# Register your models here.

admin.site.site_title="Shuxriddin"
admin.site.site_header = "Shuxriddin Test Site"

admin.site.register(FoodApp)

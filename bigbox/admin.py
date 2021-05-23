from django.contrib import admin
from .models import Box, Activity, Category, Reason

# Register your models here.
admin.site.register(Box)
admin.site.register(Activity)
admin.site.register(Category)
admin.site.register(Reason)
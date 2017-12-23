from django.contrib import admin
from .models import Event, BuildInfo

# Register your models here.

admin.site.register(Event)
admin.site.register(BuildInfo)
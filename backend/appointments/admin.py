from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'date', 'service', 'status', 'created_at')
    list_filter = ('status', 'date', 'service')
    search_fields = ('full_name', 'email')
    date_hierarchy = 'date'
    readonly_fields = ('created_at', 'updated_at')
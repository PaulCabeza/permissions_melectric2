from django.contrib import admin

from .models import State, City, Permission

# Register your models here.

admin.site.register(State)
admin.site.register(City)
# admin.site.register(Permission)

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('permission_number', 'city')
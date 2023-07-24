from django.contrib import admin
from .models import PermittedUser, AlienUser


@admin.register(PermittedUser)
class PermittedUserAdmin(admin.ModelAdmin):
    list_display = ("time_login",)
    fields = ("username", "type_of_log", "userdomain", "hostname", "ipaddress", "type_of_service", "time_login")
    readonly_fields = ("time_login",)


@admin.register(AlienUser)
class AlienUserAdmin(admin.ModelAdmin):
    list_display = ("time_login",)
    fields = (
    "username", "type_of_log", "userdomain", "hostname", "ipaddress", "type_of_service", "time_login", "session_ip")
    readonly_fields = ("time_login",)

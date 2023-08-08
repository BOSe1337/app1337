from django.contrib import admin
from .models import PermittedUser


@admin.register(PermittedUser)
class PermittedUserAdmin(admin.ModelAdmin):
    list_display = (
        "username", "type_of_log", "userdomain", "hostname", "ipaddress", "type_of_service", "time_login",
        "localdatetime", "session_ip")
    fields = (
        "username", "type_of_log", "userdomain", "hostname", "ipaddress", "type_of_service", "time_login",
        "localdatetime", "session_ip")
    readonly_fields = ("time_login",)

    search_fields = ("username", "type_of_log", "userdomain", "hostname", "ipaddress", "type_of_service", "time_login",
        "localdatetime", "session_ip")



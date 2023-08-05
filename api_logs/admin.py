from django.contrib import admin
from .models import PermittedUser, AlienUser


@admin.register(PermittedUser)
class PermittedUserAdmin(admin.ModelAdmin):
    list_display = (
        "username", "type_of_log", "userdomain", "hostname", "ipaddress", "type_of_service", "time_login",
        "localdatetime")
    fields = (
        "username", "type_of_log", "userdomain", "hostname", "ipaddress", "type_of_service", "time_login",
        "localdatetime")
    readonly_fields = ("time_login",)
    list_filter = (
        "username", "type_of_log", "userdomain", "hostname", "ipaddress", "type_of_service", "time_login",
        "localdatetime")
    search_fields = ("username", "type_of_log", "userdomain", "hostname", "ipaddress", "type_of_service", "time_login",
        "localdatetime")

@admin.register(AlienUser)
class AlienUserAdmin(admin.ModelAdmin):
    list_display = ("username", "type_of_log", "userdomain", "hostname", "ipaddress", "type_of_service", "time_login",
                    "localdatetime", "session_ip")
    fields = (
        "username", "type_of_log", "userdomain", "hostname", "ipaddress", "type_of_service", "time_login",
        "localdatetime", "session_ip")
    readonly_fields = ("time_login",)
    list_filter = ("username", "type_of_log", "userdomain", "hostname", "ipaddress", "type_of_service", "time_login",
                   "localdatetime", "session_ip")
    search_fields = ("username", "type_of_log", "userdomain", "hostname", "ipaddress", "type_of_service", "time_login",
        "localdatetime", "session_ip")

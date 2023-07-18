from django.contrib import admin
from .models import PermittedUser, AlienUser


@admin.register(PermittedUser)
class PermittedUserAdmin(admin.ModelAdmin):
    pass


@admin.register(AlienUser)
class AlienUserAdmin(admin.ModelAdmin):
    pass

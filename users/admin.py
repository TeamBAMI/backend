from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = [
        "username",
        "email",
        "is_staff",
        "type",
    ]

    # Make invites_left editable
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        fieldsets[0][1]["fields"] = ("username", "email", "password", "type")
        return fieldsets


admin.site.register(User, UserAdmin)

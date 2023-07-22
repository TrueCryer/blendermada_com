from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AbstactUserAdmin
from django.utils.translation import gettext as _
from .models import User


class UserAdmin(AbstactUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "country", "about")}),
        (_("Settings"), {"fields": ("send_newsletters", "send_notifications", "show_fullname", "show_email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )


admin.site.register(User, UserAdmin)

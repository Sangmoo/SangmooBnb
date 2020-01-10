from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Decorator # admin.site.register(models.User, CustomUserAdmin)
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    pass

    # list_display = ("username", "email", "gender", "langauge", "currency", "superhost")
    # list_filter = ("langauge", "currency", "superhost")

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "langauge",
                    "currency",
                    "superhost",
                )
            },
        ),
    )


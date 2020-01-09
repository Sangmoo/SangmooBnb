from django.contrib import admin
from . import models

# Decorator # admin.site.register(models.User, CustomUserAdmin)
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    list_display = ("username", "email", "gender", "langauge", "currency", "superhost")
    list_filter = ("langauge", "currency", "superhost")

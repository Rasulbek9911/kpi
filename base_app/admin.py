from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    model = models.CustomUser

    list_display = ['username', 'first_name',
                    'last_name', 'email', 'phone', 'image', 'position', 'section', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'image', 'position', 'section',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'image', 'position', 'section',)}),
    )


admin.site.register(models.CustomUser, CustomUserAdmin)
admin.site.register(models.Section)
admin.site.register(models.Management)
admin.site.register(models.SubstituteDirector)
admin.site.register(models.Director)
admin.site.register(models.Xodim)

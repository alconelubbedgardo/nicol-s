from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'first_name', 'last_name', 'dni', 'email','ROLE_CHOICES',)
#     fieldsets:



admin.site.register(User, UserAdmin)

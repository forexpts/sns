from django.contrib import admin
from .models import Account, Follow
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Account, UserAdmin)
admin.site.register(Follow)
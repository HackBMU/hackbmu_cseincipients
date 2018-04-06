from django.contrib import admin
from travel.models import UserProfile

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserAdmin)
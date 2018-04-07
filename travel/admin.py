from django.contrib import admin
from travel.models import UserProfile,Vendors,Vendor_services, user_services

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    pass

class VendorAdmin(admin.ModelAdmin):
    pass

class VendorServiceAdmin(admin.ModelAdmin):
    pass

class UserServiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserAdmin)
admin.site.register(Vendors, VendorAdmin)
admin.site.register(Vendor_services, VendorServiceAdmin)
admin.site.register(user_services, UserServiceAdmin)
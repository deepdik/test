from django.contrib import admin

# Register your models here.
from meenfee.models import *

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class UserOtherInfoInline(admin.StackedInline):
    model = UserOtherInfo
    can_delete = False
    verbose_name_plural = 'UserOtherInfos'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserOtherInfoInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)



class ServiceProviderAvailabilityInline(admin.TabularInline):
    model = ServiceProviderAvailability
    extra = 1
    verbose_name_plural = 'Service Provider Availability'

class ServiceAdmin(admin.ModelAdmin):
    inlines = (ServiceProviderAvailabilityInline,)


admin.site.register(Service,ServiceAdmin)
admin.site.register([Category,SubCategory,City])


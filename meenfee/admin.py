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





class MeenfeeAdmin(admin.ModelAdmin):
	list_display = ('city',)
	search_fields = ('city',)
	
class ServiceproviderAdmin(admin.ModelAdmin):
	list_display = ('firstname',)
	search_fields = ('firstname',)
	
admin.site.register(ServiceProvider,ServiceproviderAdmin)
admin.site.register(City,MeenfeeAdmin)
admin.site.register([Category,SubCategory])


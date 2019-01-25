from django.contrib import admin

# Register your models here.
from meenfee.models import(
	City,
    Category,
    SubCategory,
    ServiceProvider
	)

class MeenfeeAdmin(admin.ModelAdmin):
	list_display = ('city',)
	search_fields = ('city',)
	
class ServiceproviderAdmin(admin.ModelAdmin):
	list_display = ('firstname',)
	search_fields = ('firstname',)
	
admin.site.register(ServiceProvider,ServiceproviderAdmin)
admin.site.register(City,MeenfeeAdmin)
admin.site.register([Category,SubCategory])


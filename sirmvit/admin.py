from django.contrib import admin

# Register your models here.

from sirmvit.models import Studentdbs,Category

class YearAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, YearAdmin)

class MarksAdmin(admin.ModelAdmin):
    list_display = ['contact_no','name', 'slug','image','machine_learning','web_tech','unix','software_architecture','information_management_system','email_address', 'available', 'created', 'updated']
    list_filter = ['available','image', 'created', 'updated',]
    list_editable = ['machine_learning','web_tech','unix','software_architecture','information_management_system', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Studentdbs, MarksAdmin)

from django.contrib import admin

# Register your models here.

from sirmvit.models import Studentdbs,Category

class YearAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, YearAdmin)

class MarksAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','image','first','second','third','fourth','fifth','address', 'available', 'created', 'updated']
    list_filter = ['available','image', 'created', 'updated',]
    list_editable = ['first','second','third','fourth','fifth', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Studentdbs, MarksAdmin)

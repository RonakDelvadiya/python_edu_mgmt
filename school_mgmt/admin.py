from django.contrib import admin
from models import *

class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Student Details', {'fields': ('first_name','last_name','date_of_birth','email','address','school','roll_no','is_active','SMARTnumber')}),
    )
    ordering = ('-created_at',)
    list_display = ('first_name','last_name','date_of_birth','email','school',)
    search_fields = ('first_name','last_name','roll_no',)
    list_filter = ('is_active','school', )

class SchoolAdmin(admin.ModelAdmin):

    fieldsets = (
        ('School Details', {'fields': ('creator','name','owner','university','logo','website','is_active',)}),
    )
    ordering = ('-created_at',)
    list_display = ('creator','name','owner','university','website','is_active',)
    search_fields = ('name','university','website',)
    list_filter = ('is_active','university', )

class AddressAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Address Details', {'fields': ('street_1','street_2','city','state','country','zipcode',)}),
    )
    list_display = ('street_1','street_2','city','state','country','zipcode',)
    search_fields = ('city','street_1','street_2',)
    list_filter = ('city','state','country',)


class UniversityAdmin(admin.ModelAdmin):
    fieldsets = (
        ('University Details', {'fields': ('name','website','is_active',)}),
    )
    ordering = ('-created_at',)
    list_display = ('name','website','is_active',)
    search_fields = ('name','website',)
    list_filter = ('is_active',)

admin.site.register(Student,StudentAdmin)
admin.site.register(School,SchoolAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(University,UniversityAdmin)

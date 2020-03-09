from django.contrib import admin
from TestModel.models import *

# Register your models here.
# class ContactAdmin(admin.ModelAdmin):
#     fields = ('name', 'email')

# class ContactAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ['Main',{
#             'fields':('name','email'),
#         }],
#         ['Advance',{
#             'classes': ('collapse',), # CSS
#             'fields': ('age',),
#         }]
#     )

class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )
    list_display = ('name','age', 'email') # list
    search_fields = ('name',)
    
admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])
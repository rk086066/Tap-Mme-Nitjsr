from django.contrib import admin
from ud.models import *
# Register your models here.

# admin.site.register(User)


@admin.register(CONTACT)
class Contact_us(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'subject']
    list_per_page = (40)
    list_filter = ['email', 'name', 'subject']
    search_fields = ['email', 'name', 'subject']
    ordering = ['-created', 'email']


@admin.register(RESUME)
class Resume(admin.ModelAdmin):
    list_display = ['created', 'name', 'email', 'resume']
    list_per_page = (40)
    list_filter = ['email', 'name']
    search_fields = ['email', 'name']
    ordering = ['-created', 'email']


@admin.register(NOTICE)
class Notice(admin.ModelAdmin):
    list_display = ['created', 'subject', 'notice', 'text']
    list_per_page = (40)
    list_filter = ['subject']
    search_fields = ['subject']
    ordering = ['-created']


@admin.register(PYQS)
class PYQs(admin.ModelAdmin):
    list_display = ['created', 'company', 'question', 'note']
    list_per_page = (40)
    list_filter = ['company']
    search_fields = ['company']
    ordering = ['-created']

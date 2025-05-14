from django.contrib import admin
from django import forms
from .models import Notice, Nav, School
import nepali_datetime

# Register your models here.\


class NavbarAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


class SchoolAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not School.objects.exists()


admin.site.register(Notice)
admin.site.register(Nav, NavbarAdmin)
admin.site.register(School, SchoolAdmin)

from django.contrib import admin

# Register your models here.


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class ClearanceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'full_name', 'clearance_type', "start_date", "end_date", "job_title", "department", "employee_number",
        "gender",
        "nationality", "phone_number", "attachment", "notes", "classification", "status", 'created')


class ApprovalAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'department', 'status', "notes", "created", "updated")


class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'parent_department', 'name_ar', "name_en", "hidden")


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (  # new fieldset added on to the bottom
            'Personal Information',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'department',

                ),
            },
        ),
    )

    add_fieldsets = (
        *UserAdmin.add_fieldsets,  # original form add_fieldsets, expanded
        (
            'Personal Information',
            {
                'fields': (
                    'department',
                ),
            },
        ),
    )


admin.site.register(Clearance, ClearanceAdmin)
admin.site.register(Approval, ApprovalAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(User, CustomUserAdmin)

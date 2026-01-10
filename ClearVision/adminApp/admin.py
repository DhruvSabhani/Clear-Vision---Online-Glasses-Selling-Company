from django.contrib import admin
from adminApp.models import *
# Register your models here.

class UserAdminAdmin(admin.ModelAdmin):
    list_display=('admin_id','username','email','password','joind_date','joind_time')
    search_fields=('admin_id','username','email','password','joind_date','joind_time')
    filter_horizontal=()
    fieldsets=()

    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('admin_id','username','email','password','joind_date','joind_time'),
        }),
    )
admin.site.register(UserAdmin, UserAdminAdmin)  
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

#writing this function to make teh password field read-only
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    
    #to click on the first name
    list_display_links = ('email', 'first_name', 'last_name')
    
    readonly_fields = ('last_login', 'date_joined')
    
    # we used hypen below, for getting the descending order
    ordering = ('-date_joined',)
    
    #we need  to set these parameters for custom user model
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(Account, AccountAdmin)
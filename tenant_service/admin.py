from django.contrib import admin

from .models import Tenant, Branch

admin.site.register(Tenant)
admin.site.register(Branch)

# Register your models here.

from django.contrib import admin
from .models import List
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(List,ImportExportModelAdmin)
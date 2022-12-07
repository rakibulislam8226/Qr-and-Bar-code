from django.contrib import admin

# Register your models here.
from .models import Bar_code
class Bar_codeAdmin(admin.ModelAdmin):
  list_display = ('name', 'bar_code')
admin.site.register(Bar_code, Bar_codeAdmin)
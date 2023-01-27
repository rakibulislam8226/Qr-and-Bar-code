from django.contrib import admin

# Register your models here.
from . models import QrCode

class QrCodeAdmin(admin.ModelAdmin):
  list_display = ('name', 'qr_code')
admin.site.register(QrCode, QrCodeAdmin)
#custom Admin site end #
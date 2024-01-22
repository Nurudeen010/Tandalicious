from django.contrib import admin
from .models import Tanda, Gallery

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('email', 'complaintType', 'date_created')
    list_filter = ('complaintType', 'date_created')
    search_fields = ('email', 'complaintDetails', 'recommendation')

    class Media:
        css = {
            'all': ('css/admin.css',),
        }

admin.site.register(Tanda, ComplaintAdmin)
admin.site.register(Gallery)

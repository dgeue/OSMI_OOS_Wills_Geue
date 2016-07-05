#from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite

from django.contrib import admin

from hotel.models import zimmer, buchung, kunden

#class ReviewAdmin(admin.ModelAdmin):
#    model = buchung
    #list_display = ('wine', 'rating', 'user_name', 'comment', 'pub_date')
    #list_filter = ['pub_date', 'user_name']
    #search_fields = ['comment']

class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'

admin.site.register(zimmer)
admin.site.register(buchung)
admin.site.register(kunden)

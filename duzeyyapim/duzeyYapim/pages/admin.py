from django.contrib import admin
from . models import Contact
# Register your models here.



class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','phone','email','dept','ileti_tarihi')
    search_fields = ['first_name', 'phone','ileti_tarihi','email']

admin.site.register(Contact,ContactAdmin)
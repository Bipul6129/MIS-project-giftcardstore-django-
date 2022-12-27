from django.contrib import admin
from .models import user_invoice
# # Register your models here.

class Adminuserinvoice(admin.ModelAdmin):
    list_display = ('user','invoice','itemid','created','delivered')


admin.site.register(user_invoice,Adminuserinvoice)
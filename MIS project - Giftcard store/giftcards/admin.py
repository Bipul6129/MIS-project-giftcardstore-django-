from django.contrib import admin
from .models import Giftcards,GiftcardType,Categories
# Register your models here.

class AdminGiftcard(admin.ModelAdmin):
    list_display = ('type','posted','to')

class AdminGiftcardType(admin.ModelAdmin):
    list_display = ('name','balance','price')





admin.site.register(Giftcards,AdminGiftcard)
admin.site.register(GiftcardType,AdminGiftcardType)
admin.site.register(Categories)
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CardSet)
admin.site.register(CardCategory)

class CardContentAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
class CardAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(CardContent,CardContentAdmin)
admin.site.register(Card,CardAdmin)
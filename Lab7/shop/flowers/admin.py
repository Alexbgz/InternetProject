from django.contrib import admin
from .models import Catalog

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('product', 'category', 'price', 'quantity', 'foto')
    list_filter = ('category',)
    search_fields = ['product']

admin.site.register(Catalog, PostAdmin)
from django.contrib import admin
from ecommerce.models import comprador

class Compradores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'cep')
    list_display_links = ('id','nome')
    search_fields = ('nome',)

admin.site.register(comprador, Compradores)
